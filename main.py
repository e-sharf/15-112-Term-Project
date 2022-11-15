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
    app.background  = app.loadImage("background_image.jpg")
    app.background = app.scaleImage(app.background, 7/5)

def keyPressed(app, event):
    pass

def mousePressed(app,event):
    pass

def timerFired(app):
    pass

def redrawAll(app, canvas):
    canvas.create_image(0, 0, image = ImageTk.PhotoImage(app.background))

runApp(width = 500, height = 800)

