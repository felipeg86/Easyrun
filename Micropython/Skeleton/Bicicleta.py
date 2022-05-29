import Candado

class Bicicleta:
    iD = 0
    estado = False
    ubicacion = 'Indefinido'
    candado = Candado()

    def reset(self):
        self.iD = 0
        self.estado = False
        self.ubicacion = 'Indefinido'
        self.candado = Candado()


