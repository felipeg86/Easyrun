import Bicicleta

class Candado:
    estado = False
    ubicacion = 'Indefinido'
    n_candado = 0
    bicicleta = Bicicleta()

    def reset(self):
        self.estado = False
        self.ubicacion = 'Indefinido'
        self.n_candado = 0
        self.bicicleta = Bicicleta()
