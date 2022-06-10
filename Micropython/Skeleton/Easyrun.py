
import Perifericos
import json
from Clases_Easyrun import Bicicleta, Candado, Persona

from displayLib import MyDisplay
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
from machine import SoftSPI

import math
import time

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

disp=MyDisplay()

Persona_1 = Persona()
Persona_2 = Persona()

Bicicleta_1 = Bicicleta()
Bicicleta_2 = Bicicleta()

Candado_1 = Candado()
Candado_2 = Candado()

#Persona_1.bicicleta_asignada = Bicicleta_1
#Persona_2.bicicleta_asignada = Bicicleta_2

Bicicleta_1.candado = Candado_1
Bicicleta_2.candado = Candado_2
Bicicleta_1.persona = Persona_1
Bicicleta_2.persona = Persona_2


Bike_avail = [Bicicleta_1, Bicicleta_2]

Bike_avail[1].candado.ubicacion = 'CyT'

for i in range(1, len(Bike_avail)):
    Bike_avail[1].candado.n_candado = i

Bike_avail[0].estado=True
#print(Bike_avail[1].persona.nombre)
#Bicicleta_1.persona.nombre = "Ana"
#print(Bike_avail[1].persona.nombre)
#Abran el Jhonny
while True:
    #Poner RST
    card_id_L_1 = Perifericos.lectura(lector_1)
    if(card_id_L_1 != None):
        print (card_id_L_1)
        with open('IDcarnet.json') as IDcarnet:
            data = json.load(IDcarnet)
            data['id'] = card_id_L_1  ###################### DATO PARA MANDAR POR WIFI EN SI1
            #### Enviar dato de carnet al SI, hacer un while para esperar la recepcion del dato y
            #### cuando este llegue seguir con el codigo

        with open('Prueba_persona.json') as Prueba_persona:
            data_prueba_persona = json.load(Prueba_persona)

        if(data_prueba_persona['cedula'] != "0"): ##NO OLVIDAR: COMPARACIONES CON JSON SE HACEN EN STRING
            if(data_prueba_persona['restricciones'] != "True"):
                for i in range(0, len(Bike_avail)):
                    if ((Bike_avail[i].estado != False)):
                        Bike_avail[i].persona.nombre = data_prueba_persona['nombre']
                        Bike_avail[i].persona.cedula = data_prueba_persona['cedula']
                        Bike_avail[i].persona.iDcarnet = data_prueba_persona['iDcarnet']
                        Bike_avail[i].persona.restricciones = data_prueba_persona['restricciones']
                        disp.printShortText('Buenas') #Fino
                        #mostrar en pantalla el numero de la bicicleta escogido
                        
                        Perifericos.servo_open(i+1)
                        Bike_avail[i].candado.estado = 'en_espera'
                        Bike_avail[i].estado = True
                        with open('Prestamo.json') as Prestamo:
                            data_send_prestamo = json.load(Prestamo)
                            data_send_prestamo['id_bike'] = Bike_avail[i].iD
                            data_send_prestamo['bike_state'] = Bike_avail[i].estado
                            data_send_prestamo['puesto_prestamo'] = Bike_avail[1].candado.ubicacion
                            data_send_prestamo['daños'] = Bike_avail[i].daños
                            data_send_prestamo['nombre'] = Bike_avail[i].persona.nombre
                            data_send_prestamo['cedula'] = Bike_avail[i].persona.cedula
                            data_send_prestamo['iDcarnet'] = Bike_avail[i].persona.iDcarnet
                        #### Enviar data_send_prestamo de carnet al SI, hacer un while para esperar confirmacion de receprcion
                            time_p = time.time()
                        break
            else:
                disp.printShortText('Danas todo respetame') #Fino

        else:
            disp.printShortText('Resgistrate wuon') #Fino
    else:
        disp.printShortText('Aja y que') #Fino
        #imprimir "acerque su carnet de nuevo"
        for k in range(0, len(Bike_avail)):
            card_id_Bike = Perifericos.lectura(k+2)
            #print ("El ", k+2, "      ",card_id_Bike)
            if(card_id_Bike != None):
                print(k+2, "Lector    ", card_id_Bike)
                #print(Candado_1.estado)
                #print(Candado_2.estado)
                if(Bike_avail[k].candado.estado == 'vacio'):
                    Perifericos.servo_close(k+1)
                    Bike_avail[k].candado.estado = 'ocupado'
                    #print(Candado_1.estado)
                    #print(Candado_2.estado)
                    Bike_avail[k].iD = card_id_Bike
                    Bike_avail[k].estado = False # No disponible(Prestada) = True/  Disponible(No prestada)= False
                    Bike_avail[k].daños = False # No dañada = False/ Dañada = True
                    with open('Prestamo.json') as Entrega:
                        data_send_entrega = json.load(Entrega)
                        data_send_entrega['id_bike'] = Bike_avail[k].iD
                        data_send_entrega['bike_state'] = Bike_avail[k].estado
                        data_send_entrega['daños'] = Bike_avail[k].daños
                        #### Enviar data_send_entrega de carnet al SI, hacer un while para esperar confirmacion de receprcion
                    
