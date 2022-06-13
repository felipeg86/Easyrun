import machine 
interruptCounter = 0
totalInterruptsCounter = 0
 
def callback(pin):
  global interruptCounter
  interruptCounter = interruptCounter+1
  print("Ana")
  print("interrupcion externa")
  
p25 = machine.Pin(25, machine.Pin.IN, machine.Pin.PULL_DOWN)
p25.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)
 
