from Mascota import Mascota

class Pajarito(Mascota):

    def __init__(self,nombre, dueño, canto = None):

        Mascota.__init__(nombre, dueño)

        self.canto = canto



    def saludar(self, nombre,canto):

        if self.canto is not None:
            if self.dueño == nombre:
                return canto
            return ''

        else:
            if self.dueño == nombre:
                return 'pio'
            return ''


