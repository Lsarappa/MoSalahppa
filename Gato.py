from Mascota import Mascota

class Gato(Mascota):

    def saludar(self, nombre):

        if self.dueño == nombre:
            return  'miau'
        return 'MIAU!'