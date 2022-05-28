import machine
import time
import _thread

pin2 = machine.Pin(2, machine.Pin.OUT)

def parpadeo_off():
    pin2.value(0)
    time.sleep(1)

def parpadeo_on():
    count=0
    
    while count<=5:
        pin2.value(1)
        time.sleep(1)
        parpadeo_off()
        count += 1
    
    print("Esta por morirse")
    
    if count == 6:
        _thread.exit()
    
    print("No c murio")
    

_thread.start_new_thread(parpadeo_on,())
print("Esta vivoooo")
    
