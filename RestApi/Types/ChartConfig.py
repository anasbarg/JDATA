from RestApi.Types.Chart import *


class ChartConfig:
    def __init__(self, *args):
        self.charts = [chart for chart in args if isinstance(chart, Chart)]

    def append(self, chart):
        if isinstance(chart, Chart):
            self.charts.append(chart)
        else:
            raise TypeError("Expecting argument of type: Chart")

    def to_dict(self):
        dict_ = {"charts": []}
        for chart in self.charts:
            dict_["charts"].append(chart.to_dict())
        return dict_
