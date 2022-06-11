from MQTTconnection import *
from Messages import *

client_id = "ESP32"
mqtt_server = "broker.mqttdashboard.com"
user_mqtt = "JuanFelipe"
password_mqtt = "xr8_G!pQiw2R6fC"

last_message = 0
message_interval = 1
received = True
ID = "CH10537T"

#conect_to("Juan F","qwertyuiop")
conect_to("Carlos Mario Gonzalez","Carmar15")

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    if (time.time() - last_message) > message_interval:
        if received:
            client.publish(b'SI/Validar', id(ID),True,1)
            received = False
        else:
            client.check_msg()
            received = True
        last_message = time.time()
  except OSError as e:
    restart_and_reconnect()
