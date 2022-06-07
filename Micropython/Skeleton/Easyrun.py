
import Perifericos
import json
from Clases_Easyrun import Bicicleta, Candado, Persona

#candaco_1 = Candado()
#candaco_2 = Candado()
#persona_1 = Persona()
#persona_2 = Persona()
#bicicleta_1 = Bicicleta()
#bicicleta_2 = Bicicleta()

lector_1 = 1
lector_2 = 2
lector_3 = 3

card_id_L_1 = "0"
card_id_L_3 = "0"
card_id_L_2 = "0"

Puesto_de_prestamo = 'CyT' 
#Puesto_de_prestamo = '30' 

Persona_1 = Persona
Persona_2 = Persona

Bicicleta_1 = Bicicleta
Bicicleta_2 = Bicicleta

Candado_1 = Candado
Candado_2 = Candado

Persona_1.bicicleta_asignada = Bicicleta_1
Persona_2.bicicleta_asignada = Bicicleta_2

Bicicleta_1.candado = Candado_1
Bicicleta_2.candado = Candado_2
Bicicleta_1.persona = Persona_1
Bicicleta_2.persona = Persona_2

Candado_1.bicicleta = Bicicleta_1
Candado_2.bicicleta = Bicicleta_2

Bike_avail = [Bicicleta_1, Bicicleta_2]

Bike_avail[1].candado.ubicacion = 'CyT'

for i in range(1, len(Bike_avail)):
    Bike_avail[1].candado.n_candado = i


#print(Bike_avail[1].persona.nombre)
#Bicicleta_1.persona.nombre = "Ana"
#print(Bike_avail[1].persona.nombre)


#Abran el Jhonny
while True:
    #Poner RST
    card_id_L_1 = Perifericos.lectura(lector_1)
    if(card_id_L_1 != None):
        with open('IDcarnet.json') as IDcarnet:
            data = json.load(IDcarnet)
            data['id'] = card_id_L_1  ###################### DATO PARA MANDAR POR WIFI EN SI1
            #### Enviar dato de carnet al SI, hacer un while para esperar la recepcion del dato y
            #### cuando este llegue seguir con el codigo

        with open('Prueba_persona.json') as Prueba_persona:
            data_prueba_persona = json.load(Prueba_persona)

        if(data_prueba_persona['cedula'] != 0):
            if(data_prueba_persona['restricciones'] != 0):
                for i in range(1, len(Bike_avail)):
                    if ((Bike_avail[i].estado != 0)):
                        Bike_avail[i].persona.nombre = data_prueba_persona['nombre']
                        Bike_avail[i].persona.cedula = data_prueba_persona['cedula']
                        Bike_avail[i].persona.iDcarnet = data_prueba_persona['iDcarnet']
                        Bike_avail[i].persona.restricciones = data_prueba_persona['restricciones']
                        #mostrar en pantalla el numero de la bicicleta escogido
                        card_id_L_Bike = None
                        while (card_id_L_Bike == None) #Se asegura leer la identificación de la bicicleta a prestar
                            card_id_L_Bike = Perifericos.lectura(i+1)

                        Perifericos.servo_open(i)
                        Bike_avail[i].candado.estado = 'en_espera'
                        Bike_avail[i].estado = False
                        Bike_avail[i].daños = False
                        with open('Prestamo.json') as Prestamo:
                            data_send_prestamo = json.load(Prestamo)
                            data_send_prestamo['id_bike'] = card_id_L_Bike
                            data_send_prestamo['bike_state'] = ~Bike_avail[i].estado
                            data_send_prestamo['puesto_prestamo'] = Bike_avail[1].candado.ubicacion
                            data_send_prestamo['daños'] = Bike_avail[i].daños
                            data_send_prestamo['nombre'] = Bike_avail[i].persona.nombre
                            data_send_prestamo['cedula'] = Bike_avail[i].persona.cedula
                            data_send_prestamo['iDcarnet'] = Bike_avail[i].persona.iDcarnet
                        #### Enviar dato de carnet al SI, hacer un while para esperar confirmacion de receprcion

                        break
            else:
                ####PONER LLAMADO DE FUNCION DISPLAY
                a = 1
        else:
            ####PONER LLAMADO DE FUNCION DISPLAY
            a = 2

