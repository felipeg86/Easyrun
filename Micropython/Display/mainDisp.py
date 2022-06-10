from displayLib import MyDisplay
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
from machine import SoftSPI
import math
import time

disp=MyDisplay()
disp.printShortText('Por que eres tan crack?')