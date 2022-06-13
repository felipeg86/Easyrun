
import Perifericos
from Perifericos import MyDisplay
import json
import machine
from Clases_Easyrun import Bicicleta, Candado, Persona

from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
from machine import SoftSPI

import math
import time


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

Bicicleta_1.candado = Candado_1
Bicicleta_2.candado = Candado_2
Bicicleta_1.persona = Persona_1
Bicicleta_2.persona = Persona_2


Bike_avail = [Bicicleta_1, Bicicleta_2]

Bike_avail[1].candado.ubicacion = 'CyT'

for i in range(1, len(Bike_avail)):
    Bike_avail[1].candado.n_candado = i



timer_1 = machine.Timer(0)
timer_2 = machine.Timer(0)

Bicicleta_entrega = 0
interruptCounter_1 = 0

def Reporte_bike_1(pin):
    Bike_avail[0].danos = True # No dañada = False/ Dañada = True
    with open('Devolucion_auto.json') as Devolucion:
            data_send_devolucion = json.load(Devolucion)
            data_send_devolucion['id_bike'] = Bike_avail[0].iD
            data_send_devolucion['danos'] = Bike_avail[0].danos
            data_send_devolucion['punto_de_prestamo'] = Bike_avail[0].candado.ubicacion
            #### Enviar data_send_devolucion de carnet al SI, hacer un while para esperar confirmacion
    print("Esto es una interrupcion externa")

Danos_Bike_1 = machine.Pin(25, machine.Pin.IN, machine.Pin.PULL_DOWN)
Danos_Bike_1.irq(trigger=machine.Pin.IRQ_FALLING, handler=Reporte_bike_1)

def Reporte_bike_2(pin):
    Bike_avail[1].danos = True # No dañada = False/ Dañada = True
    with open('Devolucion_auto.json') as Devolucion:
            data_send_devolucion = json.load(Devolucion)
            data_send_devolucion['id_bike'] = Bike_avail[1].iD
            data_send_devolucion['danos'] = Bike_avail[1].danos
            data_send_devolucion['punto_de_prestamo'] = Bike_avail[1].candado.ubicacion
            #### Enviar data_send_devolucion de carnet al SI, hacer un while para esperar confirmacion
    print("Esto es una interrupcion externa_B2")

Danos_Bike_2 = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_DOWN)
Danos_Bike_2.irq(trigger=machine.Pin.IRQ_FALLING, handler=Reporte_bike_2)


def Interrupt_T1(timer_1):
    print("interrupcion")
    global interruptCounter_1
    interruptCounter_1 = interruptCounter_1 + 1
    card_id_Bike_interr_1 = Perifericos.lectura(Bicicleta_entrega+2)
    if(card_id_Bike_interr_1 == None):
        timer_1.deinit()
        Bike_avail[i].candado.estado = 'vacio'
        interruptCounter_1 = 0
        print("Se llevaron la cicla sumercé")
        with open('Prestamo_normal.json') as Prestamo_normal:
            data_send_prestamo_normal = json.load(Prestamo_normal)
            data_send_prestamo_normal['id_bike'] = Bike_avail[Bicicleta_entrega].iD
            data_send_prestamo_normal['cedula'] = Bike_avail[Bicicleta_entrega].persona.cedula
            #### Enviar data_send_prestamo_normal de carnet al SI, hacer un while para esperar confirmacion de receprcion
        
    if(interruptCounter_1>=3):
        Perifericos.servo_close(Bicicleta_entrega+1)
        interruptCounter_1 = 0
        with open('Devolucion_auto.json') as Devolucion:
            data_send_devolucion = json.load(Devolucion)
            data_send_devolucion['id_bike'] = Bike_avail[Bicicleta_entrega].iD
            data_send_devolucion['danos'] = Bike_avail[Bicicleta_entrega].danos
            data_send_devolucion['punto_de_prestamo'] = Bike_avail[Bicicleta_entrega].candado.ubicacion
            #### Enviar data_send_devolucion de carnet al SI, hacer un while para esperar confirmacion de receprcion
        timer_1.deinit()
     
def Interrupt_T2(timer_2):
    timer_2.deinit()
    vect_aux = ["Buenos", "dias"]
    for k in range(0, len(Bike_avail)):
        vect_aux[k] = Perifericos.lectura(k+2)
    with open('Prestamo_operario.json') as Prestamo_operario:
        data_send_devolucion = json.load(Prestamo_operario)
        data_send_prestamo_normal['cedula'] = Bike_avail[0].persona.cedula
        data_send_devolucion['id_bikes'] = vect_aux
        data_send_devolucion['punto_de_prestamo'] = Bike_avail[i].candado.ubicacion
        


Bike_avail[0].estado=True

Bike_avail[0].candado.estado = 'ocupado'
Bike_avail[1].candado.estado = 'vacio'

#frecuency=50
#duty_cicle=0
#servo=machine.PWM(machine.Pin(17), frecuency, duty_cicle)

#print(servo)
#print(servo.duty())

#Abran el Jhonny

while True:  
    ##Aqui va la revision de las interrupciones por hardware
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
            #print(data_prueba_persona['restricciones'] != "True")
            if(data_prueba_persona['user_type'] == "Estudiante"):  
                if((data_prueba_persona['restricciones'] != "True") and (data_prueba_persona['current_use'] == "False")):
                    for i in range(0, len(Bike_avail)):
                        if ((Bike_avail[i].estado != False)):
                            Bike_avail[i].persona.cedula = data_prueba_persona['cedula']
                            print(Bike_avail[i].estado != False)
                            disp.printShortText('Buenas') #Fino
                            #mostrar en pantalla el numero de la bicicleta escogido
                            
                            Perifericos.servo_open(i+1)
                            Bike_avail[i].candado.estado = 'en_espera'
                            Bike_avail[i].estado = True
                            
                            Bicicleta_entrega=i
                            timer_1.init(period=10000, mode=machine.Timer.PERIODIC, callback=Interrupt_T1) #Activación de interrupción para prestamo   
                            break
                else:
                    disp.printShortText('Tiene restricciones') #Fino
            elif (data_prueba_persona['user_type'] == "Operario"):
                if(data_prueba_persona['restricciones'] != "True"):
                    
                    disp.printShortText('Puede retirar las bicicletas') #Fino
                    for i in range(0, len(Bike_avail)):
                        Bike_avail[i].persona.cedula = data_prueba_persona['cedula']
                        Perifericos.servo_open(i+1)
                        Bike_avail[i].candado.estado = 'en_espera'
                        Bike_avail[i].estado = True

                    timer_2.init(period=20000, mode=machine.Timer.PERIODIC, callback=Interrupt_T2) #Activación de interrupción para prestamo a operario 
        else:
            disp.printShortText('No esta registrado') #Fino
    else:
        disp.printShortText('Aceque su carnet') #Fino
        #imprimir "acerque su carnet de nuevo"
        for k in range(0, len(Bike_avail)):
            card_id_Bike = Perifericos.lectura(k+2)
            #print ("El ", k+2, "      ",card_id_Bike)
            if(card_id_Bike != None):
                print(k+2, "Lector    ", card_id_Bike)
                if(Bike_avail[k].candado.estado == 'vacio'):
                    
                    Perifericos.servo_close(k+1)
                    Bike_avail[k].candado.estado = 'ocupado'
                    print(Bike_avail[k].candado.estado)
                    Bike_avail[k].iD = card_id_Bike
                    Bike_avail[k].estado = False # No disponible(Prestada) = True/  Disponible(No prestada)= False
                    Bike_avail[k].danos = False # No dañada = False/ Dañada = True
                    with open('Devolucion_auto.json') as Devolucion:
                        data_send_devolucion = json.load(Devolucion)
                        data_send_devolucion['id_bike'] = Bike_avail[i].iD
                        data_send_devolucion['danos'] = Bike_avail[i].danos
                        data_send_devolucion['punto_de_prestamo'] = Bike_avail[i].candado.ubicacion
                        #### Enviar data_send_devolucion de carnet al SI, hacer un while para esperar confirmacion 
