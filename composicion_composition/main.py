#/usr/bin/python
class Motor(object):

    def __init__(self, cilindraje, tipo):
        self.cilindraje = cilindraje
        self.tipo = tipo


class Rueda(object):

    def __init__(self, diametro):
        self.diametro = diametro


class Motocicleta(object):

    def __init__(self, cilindraje, tipo_motor, diametro_rueda):
        self.motor = Motor(cilindraje, tipo_motor)
        self.rueda = Rueda(diametro_rueda)

    def imprimir_cilindraje(self):
        print "cilindraje=", self.motor.cilindraje


akt_evo = Motocicleta('150cc', 'OHV', '19')
akt_evo.imprimir_cilindraje()
