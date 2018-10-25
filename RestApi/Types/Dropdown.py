class Dropdown:
    label = ""
    def __init__(self, **kwargs):
        
        # handeling required atrributes
        try:
            self.items = kwargs["items"]
        except KeyError as e:
            print(f'{e} is required to create an object of type: Dropdown')
        
        # handeling optional atrributes
        if "label" in kwargs:
            self.label = kwargs["label"]
    
    def to_dict(self):
        dict_ = {}
        dict_["items"] = self.items
        dict_["label"] = self.label
        dict_["type"] = "dropdown"
        return dict_