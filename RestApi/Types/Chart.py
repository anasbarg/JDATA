from typing import List, Dict, Tuple
from RestApi.Types.Slider import *
from RestApi.Types.Axis import *
from RestApi.Types.Dataset import *
from RestApi.Types.Dropdown import *
from RestApi.Types.ControllersList import *

class Chart:
    subtitle = ""
    type = "line"
    fill_between = False
    point_radius = 2
    display_points = True
    display_legend = False
    animation = True
    display_grid = True
    def __init__(self, **kwargs):
        # handling required kwargs
        try:
            self.title : str = kwargs["title"]
            self.data_provider : str = kwargs["data_provider"]
            self.controllers : ControllersList = kwargs["controllers"]
            self.yAxis : Axis = kwargs["yAxis"]
            self.xAxis : Axis = kwargs["xAxis"]
            self.datasets : List[Dataset] = kwargs["datasets"]
        except KeyError as e:
            print(f'{e} is required to create an object of type: Chart')
        
        # handling optional kwargs
        if "subtitle" in kwargs:
            self.subtitle : str = kwargs["subtitle"]
        if "type" in kwargs:
            self.type : str = kwargs["type"]
        if "fill_between" in kwargs:
            self.fill_between : bool = kwargs["fill_between"]
        if "point_radius" in kwargs:
            self.point_radius : float = kwargs["point_radius"]
        if "display_points" in kwargs:
            self.display_points : bool = kwargs["display_points"]
        if "display_legend" in kwargs:
            self.display_legend : bool = kwargs["display_legend"]
        if "animation" in kwargs:
            self.animation : bool = kwargs["animation"]
        if "display_grid" in kwargs:
            self.display_grid : bool = kwargs["display_grid"]
    
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
        dict_["datasets"] = [dataset.to_dict() for dataset in self.datasets]
        return dict_
