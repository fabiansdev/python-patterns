#/usr/bin/python
class Serpiente(object):
    
    def mov_izquierda(self):
        print "moviendose a la izquierda"

    def mov_derecha(self):
        print "moviendose a la derecha"


class Piton(Serpiente):
    
    def constriccion(self):
        print "le estoy apretando los huesitos"


class Cobra(Serpiente):

    def morder(self):
        print "te clave mis colmillitos"

serpiente = Serpiente()
serpiente.mov_derecha()

cobra = Cobra()
cobra.mov_izquierda()
cobra.morder() 
