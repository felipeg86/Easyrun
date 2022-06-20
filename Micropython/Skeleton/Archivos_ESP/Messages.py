import json
def id(ID_person):
    msg = {
        "Source": "ESP32",
        "ID_person": ID_person
    }
    return json.dumps(msg)
def borrow(ID_person, ID_cycle):
    msg = {
        "Source": "ESP32",
        "ID_person": ID_person,
        "ID_cycle": ID_cycle
    }
    return json.dumps(msg)
def recieve(ID_cycle, place, condition):
    msg = {
        "Source": "ESP32",
        "ID_cycle": ID_cycle,
        "Place": place,
        "condition": condition
    }
    return json.dumps(msg)

def distribute(ID_stuff,ID_cycle,place):
    msg = {
        "Source": "ESP32",
        "ID_stuff": ID_stuff,
        "ID_cycle": ID_cycle,
        "Place": place
    }
    return json.dumps(msg)
