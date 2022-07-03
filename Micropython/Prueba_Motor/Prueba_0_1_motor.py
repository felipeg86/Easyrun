from machine import Pin, PWM
import time 
servo=PWM(Pin(16))
servo.freq(50)
servo.duty(120)
time.sleep(1)
servo.duty(0)

