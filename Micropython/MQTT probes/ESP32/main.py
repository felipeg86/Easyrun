from MQTTconnection import *
from Messages import *

client_id = "ESP32"
mqtt_server = "broker.mqttdashboard.com"

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
            client.publish(b'SI/Validate', id(client_id, ID),True,1)
            client.publish(b'SI/Easyrun/Borrow',
                borrow(client_id, ID_person, ID_cycle, place),True,1)
            client.publish(b'SI/Easyrun/GetBack',
                receive(client_id, ID_person, ID_cycle, place, condition),True,1)
            client.publish(b'SI/Easyrun/Distribute',
                distribute(client_id, ID_stuff,ID_cycle,place),True,1)
            received = False
        else:
            client.check_msg()
            print(msg_received["ID_Carnet"])
            print(msg_received["ID"])
            print(msg_received["Current_Use"])
            print(msg_received["Restriction"])
            print(msg_received["User_Type")
            received = True
        last_message = time.time()
  except OSError as e:
    restart_and_reconnect()
