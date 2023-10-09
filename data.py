import pyodbc
import sqlite3

class SourceDataDemo:

    def __init__(self):
        self.title = '空间利用率情况展示'
        self.echarts3_1_data = {
            'title': '当前图书馆在馆人员情况',
            'data': [
                {"name": "本科生", "value": 47},
                {"name": "研究生", "value": 52},
                {"name": "博士生", "value": 90},
                {"name": "教职工", "value": 84},
            ]
        }
        self.echarts3_2_data = {
            'title': '图书馆各学院人员情况',
            'data': [
                {"name": "本科生院（素质教育基地/招生办/教学评估中心）", "value": 4},
                {"name": "材化学院", "value": 88},
                {"name": "船舶学院", "value": 121},
                {"name": "动力学院", "value": 122},
                {"name": "航建学院", "value": 58},
                {"name": "核学院", "value": 90},
                {"name": "机电学院", "value": 82},
                {"name": "计算机学院（保密学院/软件学院）", "value": 139},
                {"name": "经管学院", "value": 100},
                {"name": "联合学院", "value": 30},
                {"name": "马克思主义学院", "value": 24},
                {"name": "南海研究院", "value": 3},
                {"name": "青岛基地", "value": 4},
                {"name": "人文学院", "value": 81},
                {"name": "软件学院", "value": 58},
                {"name": "数学科学学院", "value": 46},
                {"name": "水声学院", "value": 173},
                {"name": "体育部", "value": 3},
                {"name": "外国语学院", "value": 45},
                {"name": "未来技术学院", "value": 11},
                {"name": "物理与光电工程学院", "value": 78},
                {"name": "信通学院", "value": 108},
                {"name": "烟台研究院", "value": 5},
                {"name": "智能科学与工程学院", "value": 196},
            ]
        }
        self.echart4_data = {
            'title': '空间利用率时间变化趋势',
            'data': [
                {"name": "在馆", "value": [30, 60, 80, 60, 55, 30, 50, 70, 50, 80, 70, 60, 50, 40]},
                {"name": "", "value": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                {"name": "", "value": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                {"name": "", "value": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                # {"name": "研究生", "value": [50, 30, 50, 60, 10, 50, 30, 50, 60, 40, 60, 40, 80, 30]},
                # {"name": "博士生", "value": [50, 60, 20, 70, 60, 40, 60, 40, 30, 70, 40, 30, 10, 50]},
                # {"name": "教职工", "value": [40, 20, 10, 20, 40, 50, 40, 50, 20, 10, 40, 40, 70, 60]},
            ],
            'xAxis': ['08h', '09h', '11h', '12h', '13h', '14h', '15h', '16h', '17h', '18h', '19h', '20h', '21h']
        }

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart
    
    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        # self.title = '空间利用率情况展示'
        # self.echarts3_1_data = {
        #     'title': '当前图书馆在馆人员情况',
        #     'data': []
        # }
        # self.echart4_data = {
        #     'title': '空间利用率时间变化趋势',
        #     'data': [],
        #     'xAxis': []
        # }

        # # Connect to local sqlite database
        # conn = sqlite3.connect('library_data.db')
        # c = conn.cursor()

        # # Read data from sqlite database for echarts3_1_data
        # c.execute("SELECT dept, in_library FROM library_stats")
        # rows = c.fetchall()
        # for row in rows:
        #     self.echarts3_1_data['data'].append({'name': row[0], 'value': row[1]})

        # # Read data from sqlite database for echart4_data
        # c.execute("SELECT in_library, utilization_rate FROM library_stats")
        # rows = c.fetchall()
        # in_library_list = []
        # utilization_rate_list = []
        # for row in rows:
        #     in_library_list.append(row[0])
        #     utilization_rate_list.append(row[1])

        # # Calculate hourly utilization rate data for echart4_data
        # cursor = conn.cursor()
        # cursor.execute('SELECT * FROM hourly_utilization_rate')
        # hourly_utilization_rate = cursor.fetchall()
        # hour_data = []
        # for i in range(len(hourly_utilization_rate)):
        #     hour_data.append(hourly_utilization_rate[i][2])
        # self.echart4_data['data'].append({"name": "在馆", "value": hour_data})
        # self.echart4_data['data'].append({"name": "", "value": utilization_rate_list})
        # self.echart4_data['data'].append({"name": "", "value": []})
        # self.echart4_data['data'].append({"name": "", "value": []})
        # self.echart4_data['xAxis'] = [f'{i:02d}h' for i in range(8, 22)]

        # # Close connections to databases
        # conn.close()
        # cursor.close()