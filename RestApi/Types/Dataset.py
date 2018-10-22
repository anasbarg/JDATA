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
    def to_dict(self):
        dict_ = {}
        dict_["label"] = self.label
        dict_["color"] = self.color
        dict_["border_width"] = self.border_width
        dict_["fill"] = self.fill
        dict_["tension"] = self.tension
        dict_["dataset_id"] = self.dataset_id
        return dict_