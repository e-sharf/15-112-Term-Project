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
import time

###############################################################################
def appStarted(app):
    # creating images
    # image from https://unsplash.com/backgrounds/colors/black
    app.background  = app.loadImage("background_image.jpg")
    app.background = app.scaleImage(app.background, 3/4)

    # app varibles
    app.timerDelay = 30
    app.timePassed = 0
    app.moonAngle = 0
    app.inSpace = False
    app.objectSet = set()
    app.time0 = 0
    # creating character
    app.charX = app.width * random.randint(3,7)/10
    app.charY = 2 * app.height//3
    # creating firstMoon
    app.moonX1 = app.charX
    app.moonY1 = 4 * app.height//5
    app.moonR1 = random.randint(3, 5)
    # creating secondMoon
    app.moonX2 = app.width * random.randint(3,7)/10
    app.moonY2 = app.height//5
    app.moonR2 = random.randint(3, 5)   
    
    # calling object moons 
    app.firstMoon = moon(app.moonX1, app.moonY1, app.moonR1)
    app.firstMoon.createMoonImage(app)
    app.objectSet.add(app.firstMoon)
    app.secondMoon = moon(app.moonX2, app.moonY2, app.moonR2)
    app.secondMoon.createMoonImage(app)
    app.objectSet.add(app.secondMoon)
    # creating object for character
    app.astro = char(app.charX, app.charY)
    app.astro.createCharImage(app)

def keyPressed(app, event):
    if event.key == "Up" and not app.inSpace:
        app.inSpace = True
        app.time0 = time.time()
        app.astro.createVector(app.firstMoon)
    if event.key == "r":
        appStarted(app)

def mousePressed(app, event):
    pass

def timerFired(app):
    app.timePassed += app.timerDelay
    if app.timePassed % 30 == 0:
        scroll(app)
        charX1, charY1 = app.firstMoon.getImageCords()
        charX2, charY2 = app.secondMoon.getImageCords()
        if charY1 - app.height*.25 > app.height:
            app.objectSet.remove(app.firstMoon)
            app.firstMoon = moon(app.width * random.randint(3,7)/10, 0, random.randint(3, 5))
            app.firstMoon.createMoonImage(app)
            app.objectSet.add(app.firstMoon)
        if charY2 - app.height*.25 > app.height and scroll:
            app.objectSet.remove(app.secondMoon)
            app.secondMoon = moon(app.width * random.randint(3,7)/10, 0, random.randint(3, 5))
            app.secondMoon.createMoonImage(app)
            app.objectSet.add(app.secondMoon)          
        for i in app.objectSet:
            i.rotateMoon(app)
        app.astro.rotateChar()
        if app.timePassed % 40 == 0 and app.inSpace:
            app.astro.gravityPull(app)
            app.astro.moveChar(app)
            app.astro.wrapChar(app)
            app.astro.rotateChar()
            if app.astro.isCollision(app) != None:
                app.inSpace = False
                if app.astro.isCollision(app) == app.secondMoon:
                    temp = app.firstMoon
                    app.firstMoon = app.secondMoon
                    app.secondMoon = temp                
        elif app.timePassed % 30 == 0 and not app.inSpace:
            app.astro.orbitChar(app, app.firstMoon)

def redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2,
                        image = ImageTk.PhotoImage(app.background))
    for i in app.objectSet:
        i.drawMoon(app, canvas)
    app.astro.drawChar(app, canvas)

runApp(width = 500, height = 800)