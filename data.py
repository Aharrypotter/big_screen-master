
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
                {"name": "本科生", "value": [3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 2, 4, 3, 4]},
                {"name": "研究生", "value": [5, 3, 5, 6, 1, 5, 3, 5, 6, 4, 6, 4, 8, 3]},
                {"name": "博士生", "value": [5, 6, 2, 7, 6, 4, 6, 4, 3, 7, 4, 3, 1, 5]},
                {"name": "教职工", "value": [4, 2, 1, 2, 4, 5, 4, 5, 2, 1, 4, 4, 7, 6]},
            ],
            'xAxis': ['08', '09', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'],
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
