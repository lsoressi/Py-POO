class Auto:
    def andar(self):
        print("ando en 4 ruedas")


class Moto:
    def andar(self):
        print("ando en 2 ruedas")

class Camnion:
    def andar(self):
        print("ando en 18 ruedas")

def andarVehiculo(vehiculo):
    vehiculo.andar()

#auto1 = Auto()
#auto1.andar()
andarVehiculo(Auto())


#moto1 = Moto()
#moto1.andar()
andarVehiculo(Moto())


#camion1 = Camnion()
#camion1.andar()
andarVehiculo(Camnion())





        
