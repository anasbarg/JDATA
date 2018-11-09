class Dropdown:
    def __init__(self, title="", label="", items=[], label2="", items2=None, type=""):
        self.title = title
        self.items = items
        self.label = label
        self.items2 = items2
        self.label2 = label2
        self.dropdown_type = type
        self.type = "dropdown"

    def to_dict(self):
        return dict(self.__dict__)
