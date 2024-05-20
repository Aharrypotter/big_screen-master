import pyodbc
from datetime import datetime, timedelta
from flask import jsonify, Blueprint
import threading
import time
import schedule
import statistics

# Global variables
# total_inlib = 0
# total_seats = 5190
# data_points

# Connect to SQL Server
server = '172.16.1.16'
database = 'skedb2020'
username = 'skevisit'
password = 'skevisit_2017'
connectionString = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'
cnxn = pyodbc.connect(connectionString)
cnxn_daily = pyodbc.connect(connectionString)
cnxn_library_stats = pyodbc.connect(connectionString)

view_name = "todayinoutnum"
table_name = "vw_day_stat_in"

# Function to query and calculate utilization rate from SQL Server
def query_sql_server():
    global total_inlib, total_seats
    cursor = cnxn.cursor()
    cursor.execute(f'SELECT SUM(inlibrary) as total_inlib FROM {view_name}')
    total_inlib = cursor.fetchall()[0][0]
    total_seats = 5190  # Change this number to the actual number of seats in the library
    
# Function to store data and time to local sqlite database
def store_to_sqlite():
    global total_inlib, data_points
    # 用于存储每个小时的数据点列表
    data_points = {str(h):[] for h in range(8,22)}
    
    def clear_data_points():
        # 清空数据点列表
        data_points.clear()
        data_points.update({str(h):[] for h in range(8,22)})
        
    def insert_data_point():
        now = datetime.now()
        
        hour = str(now.hour)
        if hour not in data_points:
            return
        utilization_rate = round(total_inlib / total_seats * 100, 2)
        # 将当前数据点添加到对应小时数的列表中
        data_points[hour].append(utilization_rate)
        
    
    schedule.every().day.at("08:00").do(clear_data_points)
    schedule.every().hour.do(insert_data_point)
    
    while True:
        schedule.run_pending()
        time.sleep(20)


def start_threads():
    thread_sql_server = threading.Thread(target=query_sql_server)
    thread_sqlite = threading.Thread(target=store_to_sqlite)
    query_sql_server()
    # thread_sql_server.start()
    thread_sqlite.start()

# 注册蓝图
back_bp = Blueprint('back', __name__)
# Create Flask app and route for sending departmental in-library numbers to frontend

@back_bp.route('/api/dept_inlib')
def send_dept_inlib():
    # Read departmental in-library numbers from SQL Server
    try:
        cursor = cnxn.cursor()
        cursor.execute(f'SELECT dept, inlibrary FROM {view_name}')
        dept_inlib = cursor.fetchall()
        
        data = []
        for dept, inlib in dept_inlib:
            data.append({"name": dept, "value": inlib})
        # 根据 value 排序
        sorted_data = sorted(data, key=lambda x: x['value'], reverse=True)
        # 只保留前十个数据
        top_ten_data = sorted_data[:10]
        echart = {
            'title': '图书馆各学院在馆人数TOP10',
            'xAxis': [i.get("name") for i in top_ten_data],
            'data': top_ten_data,
        }
    finally:
        cursor.close()
    return jsonify(echart)

# Route for sending library stats to frontend
@back_bp.route('/api/library_stats')
def send_library_stats():
    global total_inlib, total_seats
    total_seats = 5190
    try:
        cursor = cnxn_library_stats.cursor()
        cursor.execute(f'SELECT SUM(inlibrary) as total_inlib FROM {view_name}')
        total_inlib = cursor.fetchall()[0][0]
        data = [
            {"name": "在馆人数", "value": total_inlib},
            {"name": "空闲座位数", "value": total_seats - total_inlib}
        ]
        echart = {
            'title': '当前图书馆在馆人数情况',
            'xAxis': [i.get("name") for i in data],
            # 'data': [i.get("value") for i in data],
            'data': data, #去查看echart示例，看看官方是如何调用数据的（调用数据的格式）
        }
    finally:
        cursor.close()
    return jsonify(echart)

# Route for sending hourly utilization data to frontend
@back_bp.route('/api/hourly_utilization')
def send_hourly_utilization():
    averages = {hour: statistics.mean(values) if values else 0 for hour, values in data_points.items()}
    # 按照时间点的顺序提取均值
    averages_list = [averages[hour] for hour in sorted(averages)]
    
    echart = {
        'title': '空间利用率时间变化趋势',
        'names': "时段在馆人数/总座位数",
        'xAxis': ['08h', '09h', '11h', '12h', '13h', '14h', '15h', '16h', '17h', '18h', '19h', '20h', '21h'],
        'data': averages_list,
    }
    return jsonify(echart)

# Route for sending daily utilization data to frontend
@back_bp.route('/api/daily_utilization')
def send_daily_utilization():
    global total_seats
    # Change this number to the actual number of seats in the library
    total_seats = 5190
    # 获取当前日期
    current_date = datetime.now().date()

    # 获取前七天日期列表
    date_list = [current_date - timedelta(days=i) for i in range(7, 0, -1)]
    print(date_list)
    # 查询前七天的入馆次数数据
    allnums_list = []
    for date in date_list:
        # 构建查询语句
        query = f'SELECT allnum FROM {table_name} WHERE CAST(date AS DATE) = ?'
        # 执行查询
        with cnxn_daily.cursor() as cursor:
            print(date)
            cursor.execute(query, date)
            # 获取结果
            result = cursor.fetchone()
            print(result)
            if result:
                allnums_list.append(result[0])
            else:
                allnums_list.append(0)
    # 计算百分比
    # percentage_list = [round(num / total_seats * 100, 2) for num in allnums_list]
    # 构建返回给前端的数据格式
    echart = {
        'title': '近七天入馆次数统计',
        'names': "日期",
        'xAxis': [date.strftime('%Y-%m-%d') for date in date_list],
        'data': allnums_list,
    }
    print(echart)
    return jsonify(echart)