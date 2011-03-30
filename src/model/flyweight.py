from weakref import WeakValueDictionary

"""This is a flyweight pattern for lightweight memory and object construction,
it works by using the first argument of a object construction as a key, if the
key has been created before the old instance is returned, if not the object is
constructed. 

To use this flyweight pattern, inherit from it, and paste the following
snippet into the start of the __init__ function

        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

"""

class Flyweight(object):
    def __new__(cls, id, *args, **kwargs):
        if not '_instances' in cls.__dict__:
            cls._instances = WeakValueDictionary()
        if id not in cls._instances:
            o = cls._instances[id] = object.__new__(cls)
            return o
        return cls._instances[id]
