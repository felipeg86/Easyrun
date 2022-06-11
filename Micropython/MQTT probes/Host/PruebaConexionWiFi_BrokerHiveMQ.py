import time
import json
import paho.mqtt.client as paho
from paho import mqtt

client_id = "SI"
ID = ['CH10537T','Cjadgyieb','wdbhef']
m = {
    "Source": client_id,
    "Nombre": "Juan Felipe",
    "Permisos": "Si"
}
m1 = ['Juan','Si']
m2_bytes = b'[\'Hola\',\'bien\']'
m2 = m2_bytes.decode('utf8').replace("'", '"')
a = 1


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
    
    if msg.topic == 'SI/Validar':
        if msg_dec["Source"] == "ESP32":
            print("Si está en la base de datos")
            print(msg_dec)
            print(type(msg_dec))
            time.sleep(1)
            (rc, mid)= client.publish(msg.topic,json.dumps(m),qos= 1)
    elif msg.topic == 'SI/Easyrun/Prestar':
        a = 1
    elif msg.topic == 'SI/Easyrun/Devolver':
        a = 2
    elif msg.topic == 'SI/Easyrun/Distribuir':
        a = 3
    else:
        print("No se envió nada")
        (rc, mid) = client.publish('SI/Validar',json.dumps("Hola"),qos = 1)


client = paho.Client(client_id)
client.on_connect = on_connect
client.connect("broker.mqttdashboard.com", 1883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
#client.on_publish = on_publish

# subscribe 
client.subscribe("SI/Validar", qos=1)
client.subscribe("SI/Esayrun/#", qos=1)

client.loop_start()


while True:
    #(rc, mid) = client.publish("SI/Validar", "False", qos=1)
    #time.sleep(5)
    #(rc, mid) = client.publish("notification/holu", "100", qos = 1)
    client.on_message = on_message 