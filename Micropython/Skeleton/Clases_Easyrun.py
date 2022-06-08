class Bicicleta:
    iD = 0 # Nro. Tag bicicleta
    estado = False # No disponible(Prestada) = True/  Disponible(No prestada)= False
    daños = False # No dañada = False/ Dañada = True
    ubicacion = "Indefinido" #CyT/30
    candado = 'Indefinido' #instanciaciones de objetos
    persona = 'Indefinido' #instanciaciones de objetos

    def reset(self):
        self.iD = 0
        self.estado = False
        self.ubicacion = 'Indefinido' #Quitar?
        self.candado = 'Indefinido' #Quitar?
        self.persona = 'Indefinido' 



class Candado:
    estado = 'indefinido' #en espera/ocupado/vacio
    ubicacion = 'Indefinido' #CyT/30
    n_candado = 0 #Nro. del candado 
    bicicleta = 'Indefinido' #quitar?

    def reset(self):
        self.estado = False
        self.ubicacion = 'Indefinido' #Quitar?
        self.n_candado = 0 #Quitar?
        self.bicicleta = 'Indefinido' #Quitar?


class Persona:
    nombre = 'Indefinido' #nombre persona
    cedula = 0 #cedula persona 
    iDcarnet = 0 #ID carnet persona
    restricciones = False #Restricciones de persona
    bicicleta_asignada = 'Indefinido' #Id del tag de la bicicleta asignada

    def reset(self):
        self.nombre = 'Indefinido'
        self.cedula = 0
        self.iDcarnet = 0
        self.restricciones = False
        self.bicicleta_asignada = 'Indefinido'


