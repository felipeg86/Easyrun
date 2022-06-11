import json
def id(ID_person):
    msg = {
        "Source": "ESP32",
        "ID_person": ID_person
    }
    return json.dumps(msg)
def borrow(ID_person, ID_cycle, place):
    msg = {
        "Source": "ESP32",
        "ID_person": ID_person,
        "ID_cycle": ID_cycle,
        "Place": place
    }
    return json.dumps(msg)
def receive(ID_person, ID_cycle, place, condition):
    msg = {
        "Source": "ESP32",
        "ID_person": ID_person,
        "ID_cycle": ID_cycle,
        "Place": place,
        "condition": condition
    }
    return json.dumps(msg)

def distibute(ID_stuff,ID_cycle,place):
    msg = {
        "Source": "ESP32",
        "ID_stuff": ID_stuff,
        "ID_cycle": ID_cycle,
        "#Cycles": len(ID_cycle),
        "Place": place
    }
    return json.dumps(msg)
