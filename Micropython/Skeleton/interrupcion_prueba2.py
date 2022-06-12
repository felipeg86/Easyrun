import machine
 
interruptCounter = 0
totalInterruptsCounter = 0
 
timer = machine.Timer(4)  
 
def handleInterrupt(timer):
  global interruptCounter
  interruptCounter = interruptCounter+1
 
timer.init(period=1000, mode=machine.Timer.ONE_SHOT, callback=handleInterrupt)
 
while True:
  if interruptCounter>0:
    state = machine.disable_irq()
    interruptCounter = interruptCounter-1
    machine.enable_irq(state)
 
    totalInterruptsCounter = totalInterruptsCounter+1
    print("Interrupt has occurred: " + str(totalInterruptsCounter))