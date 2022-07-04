from MQTTconnection import *
from Messages import *

# Client's identification and direction of the MQTT broker
# We use a public broker to comunicate the devices
client_id = "ESP32"

# Time to public and received in seconds
last_message = 0
message_interval = 1
send = True

# Examples to prove the system
ID = "CH10537T"
ID_person = "1000595962"
ID_cycle = "150"
ID_stuff = "1000595857"
place = "CyT"
condition = True

# Conect to a WiFi Network - conne
# function -> conect_to(SSID,PASSWORD)
conect_to("Carlos Mario Gonzalez","Carmar15")

# Try to connect and subscribe to the public broker and
# subscribe to the topics of interest. If that don't run,
# the microcontroller will restart
try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

# Loop
while True:
  try:
    if (time.time() - last_message) > message_interval:
        if send:
            # Public in all the topics that the device is subscribed
            # The publication is made by one of the 4 functions of
            # Messages.py
            client.publish(b'SI/Validate', id(client_id, ID),True,1)
            client.publish(b'SI/Easyrun/Borrow',
                borrow(client_id, ID_person, ID_cycle, place),True,1)
            client.publish(b'SI/Easyrun/GetBack',
                getBack(client_id, ID_person, ID_cycle, place, condition),True,1)
            client.publish(b'SI/Easyrun/Distribute',
                distribute(client_id, ID_stuff,ID_cycle,place),True,1)
            received = False
        else:
            # Read the message that come from SI, according to the dictionary
            # structure took into account designing
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
