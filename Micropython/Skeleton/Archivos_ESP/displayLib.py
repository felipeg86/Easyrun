from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
from machine import SoftSPI
import math
import time


#spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(23))
#display = Display(spi, dc=Pin(4), cs=Pin(22), rst=Pin(15))

class MyDisplay:
    def __init__(self):
        self.sck=18
        self.mosi=23
        self.miso=19
        self.dc=15
        self.cs=12
        self.rst=14
        self.baudrate=1000000
        self.spi=SoftSPI(baudrate=1000000, polarity=0, phase=0, sck=Pin(self.sck, Pin.OUT), mosi=Pin(self.mosi, Pin.OUT), miso=Pin(self.miso, Pin.OUT))
        self.display=Display(self.spi, dc=Pin(self.dc), cs=Pin(self.cs), rst=Pin(self.rst))
        self.font = XglcdFont('Broadway17x15.c', 17, 15)
        self.message='Bienvenido'
    def spiInit(self, sck, mosi, miso, dc, cs, rst, baudrate):
        self.sck = Pin(sck, Pin.OUT)
        self.mosi = Pin(mosi, Pin.OUT)
        self.miso = Pin(miso, Pin.OUT)
        self.dc=dc
        self.cs=cs
        self.rst=rst
        self.baudrate=baudrate
        self.spi = SoftSPI(baudrate=baudrate, polarity=0, phase=0, sck=Pin(sck, Pin.OUT), mosi=Pin(mosi, Pin.OUT), miso=Pin(miso, Pin.OUT))
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