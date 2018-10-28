from typing import List, Dict, Tuple
from RestApi.Types.Slider import *
from RestApi.Types.YAxis import *
from RestApi.Types.XAxis import *
from RestApi.Types.Dataset import *
from RestApi.Types.Dropdown import *
from RestApi.Types.ControllersList import *

class Chart:
    def __init__(self, title, data_provider, controllers, yAxis, xAxis, labels, datasets, subtitle="", type="line", fill_between=False, point_radius=2, display_points=True, display_legend=False, animation=True, display_grid=True):
        self.title = title
        self.data_provider = data_provider
        self.controllers = controllers
        self.yAxis = yAxis
        self.xAxis = xAxis
        self.labels = labels
        self.datasets = datasets
        self.subtitle = subtitle
        self.type = type
        self.fill_between = fill_between
        self.point_radius = point_radius
        self.display_grid = display_grid
        self.display_points = display_points
        self.display_legend = display_legend
        self.animation = animation
    
    def to_dict(self):
        dict_ = {}
        dict_["title"] = self.title
        dict_["subtitle"] = self.subtitle
        dict_["type"] = self.type
        dict_["fill_between"] = self.fill_between
        dict_["point_radius"] = self.point_radius
        dict_["display_points"] = self.display_points
        dict_["display_legend"] = self.display_legend
        dict_["animation"] = self.animation
        dict_["display_grid"] = self.display_grid
        dict_["data_provider"] = self.data_provider
        dict_["controllers"] = self.controllers.to_dict()
        dict_["yAxis"] = self.yAxis.to_dict()
        dict_["xAxis"] = self.xAxis.to_dict()
        dict_["labels"] = self.labels
        dict_["datasets"] = [dataset.to_dict() for dataset in self.datasets]
        return dict_