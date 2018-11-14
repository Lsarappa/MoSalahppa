from Mascota import  Mascota

class Perro (Mascota):

    def saludar(self, nombre):

        if self.dueño == nombre:
            return  'guau'
        return 'GUAU!'