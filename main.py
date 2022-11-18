# name: Ethan Sharf
# 15-112 Term Project

###############################################################################

# imports
from cmu_112_graphics import *
from char import *
from objects import *
from helpers import *
import math
import random

###############################################################################
def appStarted(app):
    # creating images
    # image from https://unsplash.com/backgrounds/colors/black
    app.background  = app.loadImage("background_image.jpg")
    app.background = app.scaleImage(app.background, 3/4)

    # app varibles
    app.timerDelay = 50
    app.timePassed = 0
    app.moonAngle = 0
    app.charX = app.width *random.randint(3,7)/10
    app.charY = 2*app.height//3
    app.moonX = app.charX
    app.moonY = 4*app.height//5
    app.moonR = random.randint(3, 5)
    app.inSpace = False
    app.objectSet = set()
    
    # calling classes for inital 
    app.firstMoon = moon(app.moonX, app.moonY, app.moonR)
    app.firstMoon.createMoonImage(app)
    app.objectSet.add(app.firstMoon)
    app.astro = char(app.charX, app.charY)
    app.astro.createCharImage(app)

def keyPressed(app, event):
    if event.key == "Up":
        app.inSpace = True
        app.astro.createVector(app, app.firstMoon)

def mousePressed(app,event):
    pass


def timerFired(app):
    app.timePassed += app.timerDelay
    if app.timePassed % 50 == 0:
        app.firstMoon.rotateMoon(app)
        app.astro.rotateChar()
        if app.timePassed % 50 == 0 and app.inSpace:
            app.astro.moveChar()
            app.astro.wrapChar(app)
            if app.astro.isCollision(app):
                app.inSpace = False
        elif app.timePassed % 50 == 0 and not app.inSpace:
            app.astro.orbitChar(app, app.firstMoon)


def redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2,
                        image = ImageTk.PhotoImage(app.background))
    app.firstMoon.drawMoon(app, canvas)
    app.astro.drawChar(app, canvas)

runApp(width = 500, height = 800)