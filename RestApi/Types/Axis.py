class Axis:
    def __init__(self, scale_label, label_color="rgb(104, 104, 104)"):
        self.label_color = label_color
        self.scale_label = scale_label

    def to_dict(self):
        return dict(self.__dict__)
