import machine
import time
 
interruptCounter = 0
totalInterruptsCounter = 0
 
timer = machine.Timer(0)  
 
def handleInterrupt(timer):
    print("interrupcion")
    global interruptCounter
    interruptCounter = interruptCounter+1
 
timer.init(period=5000, mode=machine.Timer.PERIODIC, callback=handleInterrupt)

for i in range(0,8):
    print(i)
    
time.sleep(5)
timer.deinit()
    