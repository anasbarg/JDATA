class Dataset:
    def __init__(self, dataset_id, label="", color="rgb(63,81,181)", border_width=1.0, fill=False, tension=1.0):
        self.dataset_id = dataset_id
        self.label = label
        self.color = color
        self.border_width = border_width
        self.fill = fill
        self.tension = tension

    def to_dict(self):
        return dict(self.__dict__)
