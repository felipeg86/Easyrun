import json
def id(source, ID_person):
    msg = {
        "Source": source,
        "ID_person": ID_person
    }
    return json.dumps(msg)
def borrow(source, ID_person, ID_cycle, place):
    msg = {
        "Source": source,
        "ID_person": ID_person,
        "ID_cycle": ID_cycle,
        "Place": place
    }
    return json.dumps(msg)
def receive(source, ID_person, ID_cycle, place, condition):
    msg = {
        "Source": source,
        "ID_person": ID_person,
        "ID_cycle": ID_cycle,
        "Place": place,
        "condition": condition
    }
    return json.dumps(msg)

def distribute(source, ID_stuff,ID_cycle,place):
    msg = {
        "Source": source,
        "ID_stuff": ID_stuff,
        "ID_cycle": ID_cycle,
        "#Cycles": len(ID_cycle),
        "Place": place
    }
    return json.dumps(msg)
