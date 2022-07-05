import time
import json
import paho.mqtt.client as paho
from paho import mqtt

client_id = "SI"
ID = ['CH10537T','Cjadgyieb','wdbhef']
m = {
    "Source": client_id,
    "ID_Carnet": '0X907D2343',
    "ID": "1000596512",
    "Current_Use": "False",
    "Restriction": "False",
    "User_Type": "Estudiante"
}


# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    msg_dec = json.loads(msg.payload)
    if msg.topic == 'SI/Validate':
        if msg_dec["Source"] == "ESP32":
            print("-----------------------")
            print("Información recibida: " + str(msg_dec["ID_Carnet"]))
            print("-----------------------")
            time.sleep(1)
            print("-----------------------")
            print("Información enviada: ")
            print("-----------------------")
            print('Carnet: ' + str(m["ID_Carnet"]))
            print('ID del usuario: ' + str(m["ID"]))
            print('¿Tiene una bici en prestamo? ' + str(m["Current_Use"]))
            print('¿Tiene restricciones? ' + str(m["Restriction"]))
            print('Tipo de usuario: ' + str(m["User_Type"]))
            
            (rc, mid)= client.publish(msg.topic,json.dumps(m))
    elif msg.topic == 'Easyrun/Borrow':
        if msg_dec["Source"] == "ESP32":
            print("-----------------------")
            print("Tema: Borrow - Información recibida: ")
            print("-----------------------")
            print('ID del usuario: ' + str(msg_dec["ID_person"]))
            print('ID de la bicicleta: ' + str(msg_dec["ID_cycle"]))
            print('Estación: ' + str(msg_dec["Place"]))
    elif msg.topic == 'Easyrun/GetBack':
        if msg_dec["Source"] == "ESP32":
            print("-----------------------")
            print("Tema: Get Back - Información recibida: ")
            print("-----------------------")
            print('ID del usuario: ' + str(msg_dec["ID_person"]))
            print('ID de la bicicleta: ' + str(msg_dec["ID_cycle"]))
            print('Estación: ' + str(msg_dec["Place"]))
            print('Condición: ' + str(msg_dec["Condition"]))
            
    elif msg.topic == 'Easyrun/Distribute':
        if msg_dec["Source"] == "ESP32":
            print("-----------------------")
            print("Tema: Distribute - Información recibida: ")
            print("-----------------------")
            print('ID del funcionario: ' + str(msg_dec["ID_stuff"]))
            print('ID de la bicicleta: ' + str(msg_dec["ID_cycle"]))
            print('Condición: ' + str(msg_dec["#Cycles"]))
            print('Estación: ' + str(msg_dec["Place"]))
            
    else:
        print("No llegó nada")


client = paho.Client(client_id)
client.on_connect = on_connect
client.connect("broker.mqttdashboard.com", 1883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
#client.on_publish = on_publish

# subscribe 
client.subscribe("SI/Validate", qos=1)
client.subscribe("Easyrun/#", qos=1)

client.loop_start()


while True:
    client.on_message = on_message 