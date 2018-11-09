class Checkbox:
    def __init__(self, label=""):
        self.label = label

    def to_dict(self):
        return dict(self.__dict__)
