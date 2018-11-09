class Slider:
    def __init__(self, type, pips=None, title=""):
        self.slider_type = type
        self.pips = pips
        self.title = title
        self.type = "slider"

    def to_dict(self):
        return dict(self.__dict__)
