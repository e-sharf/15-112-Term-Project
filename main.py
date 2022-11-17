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
    # image from https://unsplash.com/backgrounds/colors/black
    app.background  = app.loadImage("background_image.jpg")
    app.background = app.scaleImage(app.background, 3/4)
    # image from https://www.vectorstock.com/royalty-free-vector/
    # full-moon-cartoon-vector-4118531
    app.moon = app.loadImage("moon_image.png")
    app.moon = app.scaleImage(app.moon, 1/3)
    # image from https://www.123rf.com/photo_129268090_cute-cartoon-astronaut-
    # on-the-moon-on-a-space-background.html
    app.astronaut = app.loadImage("astronaut_image.png")
    app.astronaut = app.scaleImage(app.astronaut, 1/5)

    app.timerDelay = 100
    app.timePassed = 0
    app.moonAngle = 0

def keyPressed(app, event):
    pass

def mousePressed(app,event):
    pass

def timerFired(app):
    app.timePassed += app.timerDelay
    if app.timePassed >= 400:
        app.moonAngle += .25
        app.moon = app.moon.rotate(app.moonAngle)
        app.timePassed = 0 
        if app.moonAngle >= 360:
            app.moonAngle = app.moonAngle - 360

def redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2,
                        image = ImageTk.PhotoImage(app.background))
    canvas.create_image(app.width//2, app.height//2,
                        image = ImageTk.PhotoImage(app.moon))
    canvas.create_image(app.width//2, app.height//3,
                        image = ImageTk.PhotoImage(app.astronaut))
    
    getBounds(app.moon, app.width, app.height, app.width//2, app.height//2)

runApp(width = 500, height = 800)
