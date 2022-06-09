from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
from machine import SoftSPI
import time


#spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(23))
#display = Display(spi, dc=Pin(4), cs=Pin(22), rst=Pin(15))

class MyDisplay:
    def __init__(self):
        self.sck=22
        self.mosi=19
        self.miso=23
        self.dc=18
        self.cs=15
        self.rst=4
        self.baudrate=1000000
        self.spi=SoftSPI(baudrate=1000000, polarity=0, phase=0, sck=Pin(self.sck, Pin.OUT), mosi=Pin(self.mosi, Pin.OUT), miso=Pin(self.miso, Pin.OUT))
        self.display=Display(self.spi, dc=Pin(self.dc), cs=Pin(self.cs), rst=Pin(self.rst))
        self.font = XglcdFont('fonts/Broadway17x15.c', 17, 15)
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
    def printText(self):
        print('Debe imprimir texto')
        self.display.clear(color565(204, 53, 94)) # color de fondo en RGB de 24 bits
        self.display.draw_text(55, 90, 'Hola', self.font, color565(255, 255, 255), color565(204, 53, 94))# x, y, texto, fuente, color de letra, color de fondo de letra
        time.sleep(20)
        self.display.cleanup()
        self.display.reset_mpy()