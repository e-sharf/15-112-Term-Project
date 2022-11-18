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
    # creating images
    # image from https://unsplash.com/backgrounds/colors/black
    app.background  = app.loadImage("background_image.jpg")
    app.background = app.scaleImage(app.background, 3/4)

    # image from https://www.123rf.com/photo_129268090_cute-cartoon-astronaut-
    # on-the-moon-on-a-space-background.html
    app.astronaut = app.loadImage("astronaut_image.png")
    app.astronaut = app.scaleImage(app.astronaut, 1/5)
    app.charRotate = app.astronaut

    # app varibles
    app.timerDelay = 100
    app.timePassed = 0
    app.moonAngle = 0
    app.charX = app.width//2
    app.charY = 2*app.height//3
    app.moonX = app.width//2
    app.moonY = 4*app.height//5
    app.inSpace = False
     
    app.firstMoon = moon(app.moonX, app.moonY, 20)
    app.firstMoon.createMoonImage(app)

def keyPressed(app, event):
    pass

def mousePressed(app,event):
    if event.key == "Up":
        app.inSpace = True


def timerFired(app):
    app.firstMoon.rotateMoon(app)
    moveInRotation(app)
    if app.inSpace == True and app.timePassed >= 100:
        app.charX += 5

def drawMoons(app, canvas):
    pass

def redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2,
                        image = ImageTk.PhotoImage(app.background))
    app.firstMoon.drawMoon(app, canvas)
    # canvas.create_image(app.moonX, app.moonY,
    #                     image = ImageTk.PhotoImage(app.moonRotate))
    canvas.create_image(app.charX, app.charY, 
                        image = ImageTk.PhotoImage(app.charRotate))
    
    # getBounds(app.moon, app.width, app.height, app.charX, app.charY)

runApp(width = 500, height = 800)
