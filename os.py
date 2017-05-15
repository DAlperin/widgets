
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

CELLSIZE = 5

epd = Papirus()
image = Image.new('1', epd.size, WHITE)
draw = ImageDraw.Draw(image)
def generateGrid(height, width):
    gridDict = {}
    #creates dictionary for all cells
    for y in range (height / CELLSIZE):
        for x in range (width / CELLSIZE):
            gridDict[x,y] = 0 #Sets cells as dead
    return gridDict
lifeDict = generateGrid(epd.height, epd.width)
EPD_SIZE=0.0
if os.path.exists('/etc/default/epd-fuse'):
    execfile('/etc/default/epd-fuse')
if EPD_SIZE == 0.0:
    print("Please select your screen size by running 'papirus-config'.")
    
    sys.exit()

# LM75 sensor
button5  = 37
button3 = 38
button2  = 36
button1 =  40
button4 = 35
GPIO.setup(button1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, GPIO.PUD_DOWN)
def colourGrid(draw, item, lifeDict):
    x = item[0]
    y = item[1]
    y = y * CELLSIZE # translates array into grid size
    x = x * CELLSIZE # translates array into grid size
    if lifeDict[item] == 0:
        draw.rectangle(( (x, y), (x + CELLSIZE, y + CELLSIZE) ), fill=WHITE, outline=WHITE)
    if lifeDict[item] == 1:
        draw.rectangle(( (x, y), (x + CELLSIZE, y + CELLSIZE) ), fill=BLACK, outline=WHITE)
    return None
def generateGrid(height, width):
    gridDict = {}
    #creates dictionary for all cells
    for y in range (height / CELLSIZE):
        for x in range (width / CELLSIZE):
            gridDict[x,y] = 0 #Sets cells as dead
    return gridDict
def startingGridRandom(lifeDict):
    for item in lifeDict:
       lifeDict[item] = random.randint(0,1)
    return lifeDict
def getNeighbours(epd, item,lifeDict):
    neighbours = 0
    for x in range (-1,2):
        for y in range (-1,2):
            checkCell = (item[0]+x,item[1]+y)
            if checkCell[0] < (epd.width / CELLSIZE)  and checkCell[0] >=0:
                if checkCell[1] < (epd.height / CELLSIZE) and checkCell[1]>= 0:
                    if lifeDict[checkCell] == 1:
                        if x == 0 and y == 0: # negate the central cell
                            neighbours += 0
                        else:
                            neighbours += 1
    return neighbours
def tick(epd, lifeDict):
    newTick = {}
    for item in lifeDict:
        #get number of neighbours for that item
        numberNeighbours = getNeighbours(epd, item, lifeDict)
        if lifeDict[item] == 1: # For those cells already alive
            if numberNeighbours < 2: # kill under-population
                newTick[item] = 0
            elif numberNeighbours > 3: #kill over-population
                newTick[item] = 0
            else:
                newTick[item] = 1 # keep status quo (life)
        elif lifeDict[item] == 0:
            if numberNeighbours == 3: # cell reproduces
                newTick[item] = 1
            else:
                newTick[item] = 0 # keep status quo (death)
    return newTick
def main():

    epd = Papirus()
    epd.clear()

    image = Image.new('1', epd.size, WHITE)
    draw = ImageDraw.Draw(image)

    lifeDict = generateGrid(epd.height, epd.width) # creates library and Popula$
    lifeDict = startingGridRandom(lifeDict) # Assign random life

    #Colours the live cells, blanks the dead
    for item in lifeDict:
                colourGrid(draw, item, lifeDict)

while True:
    if GPIO.input(button1) == False:
        print("GOL started")

        while True: #main game loop

                #runs a tick
            lifeDict = tick(epd, lifeDict)

                #Colours the live cells, blanks the dead
            for item in lifeDict:
            	colourGrid(draw, item, lifeDict)

            print("Rendering Frame")
            epd.display(image)
            epd.partial_update()

        if __name__=='__main__':
            main()
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
