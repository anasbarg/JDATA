class Axis:
    min = None
    max = None
    def __init__(self, **kwargs):
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

    def to_dict(self):
        dict_ = {}
        dict_["min"] = self.min
        dict_["max"] = self.max
        dict_["scale_label"] = self.scale_label
        dict_["label_color"] = self.label_color
        return dict_
