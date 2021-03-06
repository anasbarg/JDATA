from RestApi.Types.Axis import Axis


class YAxis(Axis):
    def __init__(self, scale_label, min=0, max=None, label_color="rgb(104, 104, 104)",  label_size=12):
        self.scale_label = scale_label
        self.label_color = label_color
        self.min = min
        self.max = max
        self.label_size = label_size
