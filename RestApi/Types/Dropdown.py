class Dropdown:
    title = ""
    label = ""
    label2= ""
    items2 = []
    def __init__(self, **kwargs):
        
        # handeling required atrributes
        try:
            self.items = kwargs["items"]
        except KeyError as e:
            print(f'{e} is required to create an object of type: Dropdown')
        
        # handeling optional atrributes
        if "label" in kwargs:
            self.label = kwargs["label"]
        if "label2" in kwargs:
            self.label2 = kwargs["label2"]
        if "items2" in kwargs:
            self.items2 = kwargs["items2"]
        if "title" in kwargs:
            self.title = kwargs["title"]
    
    def to_dict(self):
        dict_ = {}
        dict_["items"] = self.items
        dict_["label"] = self.label
        dict_["items2"] = self.items2
        dict_["label2"] = self.label2
        dict_["title"] = self.title
        dict_["type"] = "dropdown"
        return dict_