
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
GPIO.setmode(GPIO.BOARD)

text = PapirusText()

# Write text to the screen
WHITE = 1
BLACK = 0





while True:
    if GPIO.input(button1) == False:
        ia=$(echo "ibase=16;$(i2cget -y 1 0x48 0x00 w | sed -e 's/^0x//g' | sed -n 's/\([0-9a-f][0-9a-f]\)\([0-9a-f][0-9a-f]\)/\2\1/p'| tr [[:lower:]] [[:upper:]])" | bc)
        [ $DEBUG ] && echo "IA is ${ia}"
        #    convert that to binary
        ib=$(echo "obase=2;$ia" | bc)
        [ $DEBUG ] && echo "IB is ${ib}"
        # strip last 5 bits
        ic="${ib:0:-5}"
        [$DEBUG ] && echo "IC is ${ic}"
        # if binary value is 11 bits long, number is negative (twos complement)
        if [ $(echo -en "${ic}" | wc -c) -eq 11 ]
            then
            [ $DEBUG ] && echo "Temperature is negative"
            ica=$(echo "ibase=2;${ic}" | bc)
            id=$(echo "-2048+${ica}" | bc)
        else
            id=$(echo "ibase=2;${ic}" | bc)
            fi
            [ $DEBUG ] && echo "ID is ${id}"
            ie=$(echo "scale=3;${id}*0.125" | bc)
        if=$(echo "scale=3;${ie}*1.8+32" | bc)
            echo "Temp is ${ie} deg C (${if} deg F)."
            papirus-write "Temp is ${ie} deg C (${if} deg F)."
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
