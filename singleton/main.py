#/usr/bin/python
class Singleton (object):
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print "instance do not exist"
        else:
            print "instance exist!!!", self.get_instance()

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


a = Singleton()
# After this point, an instance already exist
# Despues de este punto una instancia ya existe.
b = Singleton()
c = Singleton()
