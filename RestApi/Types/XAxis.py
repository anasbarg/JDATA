from RestApi.Types.Axis import Axis

class XAxis(Axis):
    def __init__(self, scale_label, type="category", label_color="rgb(104, 104, 104)", label_size=12):
            self.type = type
            self.scale_label = scale_label
            self.label_color = label_color
            self.label_size = label_size