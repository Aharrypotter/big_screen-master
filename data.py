
class SourceDataDemo:

    def __init__(self):
        self.title = '座位利用率情况展示'
        self.echarts3_1_data = {
            'title': '当前座位利用率情况',
            'data': [
                {"name": "本科生", "value": 47},
                {"name": "研究生", "value": 52},
                {"name": "博士生", "value": 90},
                {"name": "教职工", "value": 84},
            ]
        }
        self.echart4_data = {
            'title': '座位利用率时间变化趋势',
            'data': [
                {"name": "本科生", "value": [30, 40, 30, 40, 30, 40, 30, 60, 20, 40, 20, 40, 30, 40]},
                {"name": "研究生", "value": [50, 30, 50, 60, 10, 50, 30, 50, 60, 40, 60, 40, 80, 30]},
                {"name": "博士生", "value": [50, 60, 20, 70, 60, 40, 60, 40, 30, 70, 40, 30, 10, 50]},
                {"name": "教职工", "value": [40, 20, 10, 20, 40, 50, 40, 50, 20, 10, 40, 40, 70, 60]},
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
        self.title = '座位利用率情况展示'
