class Bicicleta:
    def __init__ (self):
        self.iD = 0 # Nro. Tag bicicleta
        self.estado = False # No disponible(Prestada) = True/  Disponible(No prestada)= False
        self.daños = False # No dañada = False/ Dañada = True
        self.ubicacion = "Indefinido" #CyT/30
        self.candado = 'Indefinido' #instanciaciones de objetos
        self.persona = 'Indefinido' #instanciaciones de objetos
    
    

    def reset(self):
        self.iD = 0
        self.estado = False
        self.persona = 'Indefinido' 



class Candado:
    def __init__ (self):
        self.estado = 'indefinido' #en espera/ocupado/vacio
        self.ubicacion = 'Indefinido' #CyT/30
        self.n_candado = 0 #Nro. del candado 

    def reset(self):
        self.estado = False
        

class Persona:
    def __init__ (self):
        self.nombre = 'Indefinido' #nombre persona
        self.cedula = 0 #cedula persona 
        self.iDcarnet = 0 #ID carnet persona
        self.restricciones = False #Restricciones de persona
        self.bicicleta_asignada = 'Indefinido' #Id del tag de la bicicleta asignada

    def reset(self):
        self.nombre = 'Indefinido'
        self.cedula = 0
        self.iDcarnet = 0
        self.restricciones = False
        self.bicicleta_asignada = 'Indefinido'


