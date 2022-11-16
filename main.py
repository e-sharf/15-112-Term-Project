# name: Ethan Sharf
# 15-112 Term Project

###############################################################################

# imports
from cmu_112_graphics import *
from char import *
from objects import *
from helpers import *
import math

###############################################################################
def appStarted(app):
    # image from https://www.pinterest.com/pin/258886678571521581/
    app.background  = app.loadImage("background_image.jpg")
    app.background = app.scaleImage(app.background, 3/4)
    # image from https://www.vectorstock.com/royalty-free-vector/
    # full-moon-cartoon-vector-4118531
    app.moon = app.loadImage("moon_image.png")
    app.moon = app.scaleImage(app.moon, 1/3)
    # image from
    app.astronaut = app.loadImage("astronaut_image.png")
    app.astronaut = app.scaleImage(app.astronaut, 1/5)

def keyPressed(app, event):
    pass

def mousePressed(app,event):
    pass

def timerFired(app):
    pass

def redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2,
                        image = ImageTk.PhotoImage(app.background))
    canvas.create_image(app.width//2, app.height//2,
                        image = ImageTk.PhotoImage(app.moon))
    canvas.create_image(app.width//2, app.height//2,
                        image = ImageTk.PhotoImage(app.astronaut))

runApp(width = 500, height = 800)

