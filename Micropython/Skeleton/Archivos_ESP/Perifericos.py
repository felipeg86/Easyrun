from mfrc522 import MFRC522
from machine import Pin
from machine import SPI
from machine import SoftSPI
from machine import PWM

from ili9341 import Display, color565
from xglcd_font import XglcdFont
import math
import time

sck=18
mosi=23
miso=19

spi=SoftSPI(baudrate=1000000, polarity=0, phase=0, sck=Pin(sck, Pin.OUT), mosi=Pin(mosi, Pin.OUT), miso=Pin(miso, Pin.OUT))
spi.init()

rdr1 = MFRC522(spi=spi, gpioRst=4, gpioCs=5)
rdr2 = MFRC522(spi=spi, gpioRst=27, gpioCs=2)
rdr3 = MFRC522(spi=spi, gpioRst=21, gpioCs=22)

def lectura(numero_lector):

    print("Place card")

    card_id="0"
    if(numero_lector==1):
        for i in range(1,10):
            (stat, tag_type) = rdr1.request(rdr1.REQIDL)
            if stat == rdr1.OK:    
                (stat, raw_uid) = rdr1.anticoll()
                if stat == rdr1.OK:
                    card_id = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                    return card_id
    elif(numero_lector==2):
        for i in range(1,10):
            (stat, tag_type) = rdr2.request(rdr2.REQIDL)
            if stat == rdr2.OK:    
                (stat, raw_uid) = rdr2.anticoll()
                if stat == rdr2.OK:
                    card_id = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                    return card_id

    elif(numero_lector==3):
        for i in range(1,10):
            (stat, tag_type) = rdr3.request(rdr3.REQIDL)
            if stat == rdr3.OK:    
                (stat, raw_uid) = rdr3.anticoll()
                if stat == rdr3.OK:
                    card_id = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                    return card_id

    else:
        card_id="0"
        print("error")
        return card_id


def servo_open(num_servo):
    if num_servo == 1:
        servo = PWM(Pin(16))
        servo.freq(50)  #Hz
        servo.duty(25)
        time.sleep_ms(400)
        servo.duty(0)
    elif num_servo == 2:
        servo = PWM(Pin(17))  #configurar pin 21 para trabajar con PWM
        servo.freq(50)  #Hz
        servo.duty(25)
        time.sleep_ms(400)
        servo.duty(0)

def servo_close(num_servo):
    if num_servo == 1:
        servo = PWM(Pin(16))  #configurar pin 21 para trabajar con PWM
        servo.freq(50)  #Hz
        servo.duty(135)
        time.sleep_ms(400)
        servo.duty(0)
    elif num_servo == 2:
        servo = PWM(Pin(17))  #configurar pin 21 para trabajar con PWM
        servo.freq(50)  #Hz
        servo.duty(135)
        time.sleep_ms(400)
        servo.duty(0)
    

class MyDisplay:
    def __init__(self):
        self.dc=15
        self.cs=12
        self.rst=14
        self.display=Display(spi, dc=Pin(self.dc), cs=Pin(self.cs), rst=Pin(self.rst))
        self.font = XglcdFont('Broadway17x15.c', 17, 15)
        self.message='Bienvenido'
    def spiInit(self, sck, mosi, miso, dc, cs, rst, baudrate):
        self.display = Display(spi, dc=Pin(dc), cs=Pin(cs), rst=Pin(rst))
        self.font = XglcdFont('fonts/Broadway17x15.c', 17, 15)
    def printShortText(self, text):
        self.display.draw_text(0, 0, text, self.font, color565(255, 255, 255), color565(204, 53, 94))# x, y, texto, fuente, color de letra, color de fondo de letra
    def printText(self, text):
        print('Debe imprimir texto')
        self.display.clear(color565(204, 53, 94)) # color de fondo en RGB de 24 bits
        self.display.draw_text(0, 0, '5', self.font, color565(255, 255, 255), color565(204, 53, 94))# x, y, texto, fuente, color de letra, color de fondo de letra
        self.display.draw_text(10, 0, '2', self.font, color565(255, 255, 255), color565(204, 53, 94))# x, y, texto, fuente, color de letra, color de fondo de letra
        ceiling=math.ceil(len(text)/23)
        counter=1
        if ceiling>1:
            aux_matrix=' '
            while len(text)>23:
                aux_matrix=[aux_matrix,
                            text[1:23]]
                text=text[24:len(text)]
                counter+=1
            if len(text)>0:
                aux_matrix=[aux_matrix,
                            text[1:len(text)]]
                counter+=1
        else:
            aux_matrix=text
            
        for x in range(counter):
            print(aux_matrix[counter])
        time.sleep(15)
        self.display.cleanup()
        self.display.reset_mpy()
        
"""
About printing text:
* 14 is recommended as difference between two lines 'y' coordinates for broadway font.
* 10 is recommended as difference between two characters 'x' coordinates for broadway font.
* A maximum of 23 characters (letters and numbers) can be printed per line
* 10*23=230 spaces in one line
"""
