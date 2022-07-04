import time
from umqttsimple import MQTTClient
from machine import *
import network as nt
import json

# Client's identification and direction of the MQTT broker
# We use a public broker to comunicate the devices
client_id = "ESP32"
mqtt_server = "broker.mqttdashboard.com"

# Global variable use to save the information of the message income
global msg_received

# Function to restart the devices in case of failure
def restart_and_reconnect():
    print('Failed to connect. Reconnecting...')
    time.sleep(5)
    machine.reset()

# Function to connect the device to a WiFi Network.
# Inside this, there is a while loop to ensure the connection
def conect_to(SSID, PASSWORD):
    try:
        sta_if = nt.WLAN(nt.STA_IF)
        sta_if.active(True)
        led = Pin(2,Pin.OUT)
        if not sta_if.isconnected():
            sta_if.active(True)
            sta_if.connect(SSID,PASSWORD)
            print("Trying to connect to the network: ",SSID)
            while not sta_if.isconnected():
                pass
        print("Connected")
        led.value(1)
    except OSError as e:
        restart_and_reconnect()

# sub_cb is used to read the message send and received, due to MQTT
# doesn't discriminate the difference of the source of the message.
# In this case, the microcontroller recieve information by the Validate
# topic.

def sub_cb(topic, msg):
    msg_dec = json.loads(msg)
    if msg_dec["Source"] == "SI":
        if topic == b'SI/Validate':
            msg_received = msg_dec

# connect_and_subscribe connect the device to a MQTT broker ans set the
# call back to received messages. Then, it's subscribe to the topics of
# interest.
# With the comand SI/Easyrun/# the ESP is subscribed to al the topics
# that have the same structure at the begin.
def connect_and_subscribe():
    global client_id, mqtt_server
    client = MQTTClient(client_id,"broker.mqttdashboard.com")
    client.connect()
    client.set_callback(sub_cb)
    client.subscribe(b'SI/Validate',1)
    client.subscribe(b'SI/Easyrun/#',1)
    print('Connected to %s MQTT broker' % (mqtt_server))
    return client
