from model.flyweight import Flyweight

class OperationServices(Flyweight):
    def __init__(self,operation_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        #TODO: Implement this