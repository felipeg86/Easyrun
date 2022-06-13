class Bicicleta:
    def __init__ (self):
        self.iD = 0 # Nro. Tag bicicleta
        self.estado = False # No disponible(Prestada) = True/  Disponible(No prestada)= False
        self.danos = False # No dañada = False/ Dañada = True
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
        self.cedula = 0 #cedula persona 
        self.bicicleta_asignada = '0x00000000' #Id del tag de la bicicleta asignada

    def reset(self):
        self.cedula = 0
        self.bicicleta_asignada = '0x00000000'


