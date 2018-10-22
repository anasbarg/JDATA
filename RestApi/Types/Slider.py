class Slider:
    pips = None
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
    
    def to_dict(self):
        dict_ = {}
        dict_["pips"] = self.pips
        dict_["label"] = self.label
        dict_["type"] = self.type
        return dict_