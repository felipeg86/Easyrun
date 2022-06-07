class Bicicleta:
    iD = 0
    estado = False
    ubicacion = "Indefinido"
    candado = 'Indefinido'
    persona = 'Indefinido'

    def reset(self):
        self.iD = 0
        self.estado = False
        self.ubicacion = 'Indefinido'
        self.candado = 'Indefinido'
        self.persona = 'Indefinido'



class Candado:
    estado = 'indefinido'
    ubicacion = 'Indefinido'
    n_candado = 0
    bicicleta = 'Indefinido'

    def reset(self):
        self.estado = False
        self.ubicacion = 'Indefinido'
        self.n_candado = 0
        self.bicicleta = 'Indefinido'




class Persona:
    nombre = 'Indefinido'
    cedula = 0
    iDcarnet = 0
    restricciones = False
    bicicleta_asignada = 'Indefinido'

    def reset(self):
        self.nombre = 'Indefinido'
        self.cedula = 0
        self.iDcarnet = 0
        self.restricciones = False
        self.bicicleta_asignada = 'Indefinido'


