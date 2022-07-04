import json

# Here are made four functions (for each topic) to build the
# structure of the sended messages to SI. Then the dictionary
# is codificated with json.


# Function id is used to send the message of the identification
# readed by the RFID sensor in the topic Validate
def id(source, ID_Carnet):
    msg = {
        "Source": source,
        "ID_Carnet": ID_Carnet
    }
    return json.dumps(msg)

# Function id is used to send the message needed in a borrow
# process to SI.
def borrow(source, ID_person, ID_cycle, place):
    msg = {
        "Source": source,
        "ID_person": ID_person,
        "ID_cycle": ID_cycle,
        "Place": place
    }
    return json.dumps(msg)

# Function id is used to send the message needed in a get back
# process to SI.

def getBack(source, ID_person, ID_cycle, place, condition):
    msg = {
        "Source": source,
        "ID_person": ID_person,
        "ID_cycle": ID_cycle,
        "Place": place,
        "condition": condition
    }
    return json.dumps(msg)

# Function id is used to send the message needed when the stuff
# need move a group of bike from a station to another.

def distribute(source, ID_stuff,ID_cycle,place):
    msg = {
        "Source": source,
        "ID_stuff": ID_stuff,
        "ID_cycle": ID_cycle,
        "#Cycles": len(ID_cycle),
        "Place": place
    }
    return json.dumps(msg)
