class ControllersList:

    header_text = "Input Controllers"
    def __init__(self, *args, **kwargs):
        #handeling optional attributes
        if "header_text" in kwargs:
            self.header_text = kwargs["header_text"]
        # required Atrribute
        try:
            self.controllers_list = list(args)
        except TypeError as e:
            print("You have to provide at least one Controller to the constructor in order to create an object of type ControllersList")
    
    def __iter__(self):
        return iter(self.controllers_list)

    def to_dict(self):
        dict_ = self.__dict__
        dict_["controllers_list"] = [controller.to_dict() for controller in self.controllers_list]
        return dict_
