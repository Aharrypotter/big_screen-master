from flask import request

class SourceDataDemo:

    def __init__(self):
        self.title = '空间利用率情况展示'
        self.echarts3_1_data = {
            'title': '当前图书馆在馆人数情况',
            'data': [
                {"name": "在馆人数", "value": 520},
                {"name": "空闲座位数", "value": 5190 - 520},
            ]
        }
        self.echarts3_2_data = {
            'title': '图书馆各学院在馆人数TOP10',
            'data': [
                {"name": "船舶学院", "value": 121},
                {"name": "航建学院", "value": 58},
                {"name": "动力学院", "value": 122},
                {"name": "智能科学与工程学院", "value": 196},
                {"name": "水声学院", "value": 173},
                {"name": "计算机学院", "value": 139},
                {"name": "机电学院", "value": 82},
                {"name": "信通学院", "value": 108},
                {"name": "经管学院", "value": 100},
                {"name": "材化学院", "value": 88},
                {"name": "数学科学学院", "value": 46},
                {"name": "物理与光电工程学院", "value": 78},
                {"name": "外国语学院", "value": 45},
                {"name": "人文学院", "value": 81},
                {"name": "核学院", "value": 90},   
                {"name": "马克思主义学院", "value": 24},
                {"name": "软件学院", "value": 58},
                {"name": "联合学院", "value": 30},
                {"name": "未来技术学院", "value": 11},
            ]
        }
        self.echart4_data = {
            'title': '空间利用率时间变化趋势',
            'data': [
                {"name": "时段在馆人数/总座位数", "value": [30, 60, 80, 60, 55, 30, 50, 70, 50, 80, 70, 0, 0]},
            ],
            'xAxis': ['08h', '09h', '11h', '12h', '13h', '14h', '15h', '16h', '17h', '18h', '19h', '20h', '21h']
        }

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': '当前图书馆在馆人数情况',
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart
    
    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        # 根据 value 排序
        sorted_data = sorted(data.get('data'), key=lambda x: x['value'], reverse=True)
        # 只保留前十个数据
        top_ten_data = sorted_data[:10]
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in top_ten_data],
            'data': top_ten_data,
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
        self.title = '空间利用率情况展示'
    
    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        data_base = self.get_data('/api/library_stats')
        echart = {
            'title': '当前图书馆在馆人数情况',
            'xAxis': [i.get("name") for i in data_base],
            'data': data_base,
        }
        return echart
    
    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        data_base = self.get_data('/api/dept_inlib')
        # 根据 value 排序
        sorted_data = sorted(data_base, key=lambda x: x['value'], reverse=True)
        # 只保留前十个数据
        top_ten_data = sorted_data[:10]
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in top_ten_data],
            'data': top_ten_data,
        }
        return echart

    @property
    def echart4(self):
        data = self.get_data('/api/daily_utilization')
        echart = {
            'title': data.get('title'),
            'names': data.get('data'),
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart
    
    def get_data(self, url):
        """
        获取后端接口返回的数据
        """
        response = request.get(f'http://localhost:5000{url}')
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None