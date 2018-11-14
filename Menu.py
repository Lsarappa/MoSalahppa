from Dueño import Dueño
from Perro import Perro
from Gato import Gato
from Pajarito import Pajarito

class Menu (object):

    lista_Mascota = []

    @staticmethod
    def iniciar ():


        print("1----ABM\n" 
              "2----Saludar\n")

        opcion = int(input())

        if opcion == 1:
            Menu.ABM(Menu)
        elif opcion == 2:
            Menu.Saludar(Menu)


    def ABM (self):

        print("1---Alta\n"
              "2---Baja\n"
              "3---Modificacion\n"
              "4---Salir\n")

        opcion = int(input())

        if opcion == 1:
            Menu.Alta(Menu)
        elif opcion == 2:
            Menu.Baja(Menu)
        elif opcion == 3:
            Menu.Modificacion(Menu)

    def Alta (self):

        print("Inserte nombre dueño")

        nombre_dueño = str(input())

        print("Inserte nombre mascota")

        nombre_mascota = str(input())

        for a in self.lista_Mascota:

            if a.nombre == nombre_mascota:

                print(self.iniciar())

        print("Inserte tipo de mascota ")

        tipo_mascota = str(input())

        dueño = Dueño(nombre_dueño)



        if tipo_mascota == "perro":
            mascota = Perro(nombre_mascota, dueño)

            self.lista_Mascota.append(mascota)


        if tipo_mascota == "gato":
            mascota = Gato(nombre_mascota, dueño)

            self.lista_Mascota.append(mascota)


        if tipo_mascota == "pajarito":

            print("ingrese canto")
            canto = str(input())

            mascota = Pajarito(nombre_mascota,dueño, canto)

            self.lista_Mascota.append(mascota)


        for a in self.lista_Mascota:
            print(a.nombre)
        self.iniciar()

    def Baja(self):

        print("Inserte nombre dueño")

        nombre_dueño = str(input())

        print("Inserte nombre mascota")

        nombre_mascota = str(input())

        for a in self.lista_Mascota:

            if a.nombre == nombre_mascota:

                if a.dueño.nombre == nombre_dueño:

                    self.lista_Mascota.remove(a)

        self.iniciar();

    def Modificacion (self):

        print("Inserte nombre dueño")

        nombre_dueño = str(input())

        print("Inserte nombre mascota")

        nombre_mascota = str(input())

        print("Insertar nuevo nombre mascota")

        nuevo_nombre_mascota = str(input())

        for a in self.lista_Mascota:

            if a.nombre == nombre_mascota:

                if a.dueño.nombre == nombre_dueño:

                    a.nombre = nuevo_nombre_mascota

        self.iniciar();

    def Saludar(self):

        print("Inserte nombre dueño")

        nombre_dueño = str(input())

        print("Inserte nombre mascota")

        nombre_mascota = str(input())

        for a in self.lista_Mascota:

            if a.dueño == nombre_dueño:

                a.saludar()
