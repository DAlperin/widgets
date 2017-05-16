
#!/usr/bin/python
#frownt = front
import os
import sys

from PIL import Image
from PIL import ImageDraw
import RPi.GPIO as GPIO
from papirus import Papirus
import random
import time

from papirus import PapirusText
from papirus import PapirusImage
imagefun = PapirusImage()
GPIO.set mode(GPIO.BOARD)

text = PapirusText()

# Write text to the screen
WHITE = 1
BLACK = 0





while True:
    if GPIO.input(button1) == False:
        print("button2 pressed")
        text.write("PaPiRus Buttons  Button 2 pressed")
    if GPIO.input(button2) == False:
        print("button2 pressed")
        text.write("PaPiRus Buttons  Button 2 pressed")
    if GPIO.input(button3) == False:
        print("button3 pressed")
        text.write("PaPiRus Buttons  Button 3 pressed")
    if GPIO.input(button4) == False:
        print("button4 pressed")
        text.write("PaPiRus Buttons  Button 4 pressed")    
    if GPIO.input(button5) == False:
        print("button5 pressed")
        text.write("PaPiRus Buttons  Button 5 pressed")  
