import time
from umqttsimple import MQTTClient
from machine import *
import network as nt
import json

client_id = "ESP32"
mqtt_server = "broker.mqttdashboard.com"
global msg_received

def restart_and_reconnect():
    print('Failed to connect. Reconnecting...')
    time.sleep(5)
    machine.reset()

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

def sub_cb(topic, msg):
    msg_dec = json.loads(msg)
    if msg_dec["Source"] == "SI":
        if topic == b'SI/Validar':
            msg_received = msg_dec["ID_person"]

def connect_and_subscribe():
    global client_id, mqtt_server
    client = MQTTClient(client_id,"broker.mqttdashboard.com")
    client.connect()
    client.set_callback(sub_cb)
    client.subscribe(b'SI/Validate',1)
    client.subscribe(b'SI/Easyrun/#',1)
    print('Connected to %s MQTT broker' % (mqtt_server))
    return client
