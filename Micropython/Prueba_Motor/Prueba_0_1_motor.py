from machine import Pin, PWM



servo=PWM(Pin(15))
servo.freq(50)
servo.duty(120)
