from typing import List, Dict, Tuple

class ChartConfig:
    def __init__(self, *args):
        self.charts = [chart for chart in args if isinstance(chart, Chart)]
    def append(chart):
        if isinstance(chart, Chart):
            self.charts.append(chart)
        else:
            raise TypeError("Expecting argument of type: Chart")

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
            self.sliders : List[Slider] = kwargs["sliders"]
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

class Slider:
    self.pips = None
    def __init__(self, **kwargs):
        # handling required kwargs
        try:
            self.label : str = kwargs["label"]
            self.type  : str = kwargs["type"]
        except KeyError as e:
            print(f'{e} is required to create an object of type: Slider')
        
        # handling optional kwargs
        if "pips" in kwargs:
            self.pips : List[int] = kwargs["pips"]

class Axis:
    min = None
    max = None
    def __init_(self, **kwargs):
        # handling required kwargs
        try:
            self.scale_label : str = kwargs["scale_label"]
            self.label_color : str = kwargs["label_color"]
        except KeyError as e:
            print(f'{e} is required to create an object of type: Axis')

        # handling optional kwargs
        if "min" in kwargs:
            self.min : int = kwargs["min"]
        if "max" in kwargs:
            self.max : int = kwargs["max"]

class Dataset:
    label = ""
    color = "rgb(63,81,181)"
    border_width = 1.0
    fill = False
    tension = 1.0
    def __init__(self, **kwargs):
        # handling required kwargs
        try:
            self.dataset_id : str = kwargs["dataset_id"]
        except KeyError as e:
            print(f'{e} is required to create an object of type: Dataset')

        # handling optional kwargs
        if "label" in kwargs:
            self.label : str = kwargs["label"]
        if "color" in kwargs:
            self.color : str = kwargs["color"]
        if "border_width" in kwargs:
            self.border_width : float = kwargs["border_width"]
        if "fill" in kwargs:
            self.fill : bool = kwargs["fill"]
        if "tension" in kwargs:
            self.tension : float = kwargs["tension"]