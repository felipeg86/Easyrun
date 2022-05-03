# More details can be found in TechToTinker.blogspot.com 
# George Bantique | tech.to.tinker@gmail.com

from mfrc522 import MFRC522
from machine import Pin
from machine import SPI
from machine import SoftSPI

# display
from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont

sck1 = Pin(18, Pin.OUT)
mosi1 = Pin(23, Pin.OUT)
miso1 = Pin(19, Pin.OUT)
spi1 = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck1, mosi=mosi1, miso=miso1)
#spi2 = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck1, mosi=mosi1, miso=miso1)

#Display
sckd = Pin(18, Pin.OUT)
mosid = Pin(23, Pin.OUT)
misod = Pin(19, Pin.OUT)
spid = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sckd, mosi=mosid, miso=misod)
display = Display(spid, dc=Pin(4), cs=Pin(15), rst=Pin(21))
broadway = XglcdFont('fonts/Broadway17x15.c', 17, 15)


spi1.init()
#spi2.init()

rdr1 = MFRC522(spi=spi1, gpioRst=22, gpioCs=5)
#rdr2 = MFRC522(spi=spi1, gpioRst=15, gpioCs=22)
#rdr3 = MFRC522(spi=spi1, gpioRst=21, gpioCs=14)
print("Place card")

display.clear(color565(204, 53, 94)) # color de fondo en RGB de 24 bits
display.draw_text(55, 90, 'Hola', broadway, color565(255, 255, 255), color565(204, 53, 94))# x, y, texto, fuente, color de letra, color de fondo de letra
display.draw_text(110, 120, 'que', broadway, color565(255, 255, 255), color565(204, 53, 94))
display.draw_text(75, 150, 'mas', broadway, color565(255, 255, 255), color565(204, 53, 94))
    
sleep(20)
display.cleanup()

while True:
    (stat, tag_type) = rdr1.request(rdr1.REQIDL)
    #(stat2, tag_type2) = rdr2.request(rdr2.REQIDL)    
    
    #if stat == rdr1.OK or stat2==rdr2.OK:
    if stat == rdr1.OK:    
        (stat, raw_uid) = rdr1.anticoll()
        if stat == rdr1.OK:
            card_id = "uid: 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print(card_id)
            
  #  (stat2, tag_type2) = rdr2.request(rdr2.REQIDL)
   # if stat2 == rdr2.OK:
    #    (stat2, raw_uid2) = rdr2.anticoll()
     #   if stat2 == rdr2.OK:
      #      card_id2 = "uid: 0x%02x%02x%02x%02x" % (raw_uid2[0], raw_uid2[1], raw_uid2[2], raw_uid2[3])
       #     print("el dos: ",card_id2)