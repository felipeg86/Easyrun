from mfrc522 import MFRC522
from machine import Pin
from machine import SPI
from machine import SoftSPI

def lectura(numero_lector):

    sck = Pin(18, Pin.OUT)
    mosi = Pin(23, Pin.OUT)
    miso = Pin(19, Pin.OUT)
    spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)

    spi.init()

    rdr1 = MFRC522(spi=spi, gpioRst=4, gpioCs=5)
    rdr2 = MFRC522(spi=spi, gpioRst=27, gpioCs=2)
    rdr3 = MFRC522(spi=spi, gpioRst=21, gpioCs=22)
    print("Place card")

    #int lector_activado;
    #int numero_lector=2;
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

        
