class Checkbox:
    label = ""
    def __init__(self, **kwargs):
        if "label" in kwargs:
            self.label = kwargs["label"]
    
    def to_dict(self):
        dict_ = {}
        dict_["label"] = self.label
        dict_["type"] = "Checkbox"
        return dict_