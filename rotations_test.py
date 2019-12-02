from ili934xnew import ILI9341, color565
from machine import Pin, SPI
import tt14

text = 'F'
spi = SPI(2, baudrate=20000000, miso=Pin(19),mosi=Pin(23), sck=Pin(18))
display = ILI9341(spi, cs=Pin(2), dc=Pin(27), rst=Pin(33), w=320, h=240, r=0)
display.erase()
display.set_font(tt14)
display.set_pos(0,0)
display.print(text)
display.set_pos(0,20)
display.print(text)
display.set_pos(40,20)
display.print(text)

