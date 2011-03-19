from weakref import WeakValueDictionary

class Flyweight(object):
    def __new__(cls, id, *args, **kwargs):
        if not '_instances' in cls.__dict__:
            cls._instances = WeakValueDictionary()
        if id not in cls._instances:
            o = cls._instances[id] = object.__new__(cls)
            return o
        return cls._instances[id]