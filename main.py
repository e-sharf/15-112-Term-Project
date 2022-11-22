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
    app.charX = app.width * random.randint(3,7) / 10
    app.charY = 2 * app.height//3
    # creating firstMoon
    app.moonX1 = app.charX
    app.moonY1 = 4 * app.height//5
    app.moonR1 = random.randint(3, 5)
    # creating secondMoon
    app.moonX2 = app.width * random.randint(3,7) / 10
    app.moonY2 = app.height//10
    app.moonR2 = random.randint(3, 5)
    # creating ufo
    app.ufoX = app.width * random.randint(3, 7) / 10 
    app.ufoY = app.height * random.randint(3, 7) / 10
    app.ufoRadius = 4 
    
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
    # creating ufo object
    app.ufo = alien(app.width, app.height, 100)
    app.ufo.createUfoImage(app)
    app.objectSet.add(app.ufo)

def keyPressed(app, event):
    if event.key == "Up" and not app.inSpace:
        app.inSpace = True
        app.time0 = time.time()
        app.astro.createVector(app.firstMoon)
    if event.key == "r":
        appStarted(app)

def mousePressed(app, event):
    pass

def createNewObject(app):
    charX1, charY1 = app.firstMoon.getImageCords()
    charX2, charY2 = app.secondMoon.getImageCords()
    if charY1 - app.height*.1 > app.height:
        app.objectSet.remove(app.firstMoon)
        app.firstMoon = moon(app.width * random.randint(30,70)/100, 
                -200, random.randint(3, 5))
        if app.firstMoon.inRadius(app) != None:
            i = app.firstMoon.inRadius(app)
            app.objectSet.remove(i)
        app.firstMoon.createMoonImage(app)
        app.objectSet.add(app.firstMoon)
    if charY2 - app.height*.15 > app.height and scroll:
        app.objectSet.remove(app.secondMoon)
        app.secondMoon = moon(app.width * random.randint(30,70)/100, 
                -150, random.randint(3, 5))
        if app.secondMoon.inRadius(app) != None:
            i = app.secondMoon.inRadius(app)
            app.objectSet.remove(i)
        app.secondMoon.createMoonImage(app)
        app.objectSet.add(app.secondMoon)

def createNewAlien(app):
    if random.randint(1, 100) <= 10:
        randX = random.randint(30,70)
        app.ufo = alien(app.width *  randX / 100, -100, 4)
        app.objectSet.add(app.ufo)
        if app.ufo.inRadius(app) == None:
            app.ufo.createUfoImage(app)
        else:
            app.objectSet.remove(app.ufo)

def deleteAlien(app):
    newSet = app.objectSet
    for i in app.objectSet:
        charX, charY = i.getImageCords()
        if charY - app.height*.25 > app.height and isinstance(i, alien):
            continue
        else:
            newSet.add(i)
    app.objectSet = newSet

def timerFired(app):
    app.timePassed += app.timerDelay
    if app.timePassed % 30 == 0:
        scroll(app)
        createNewObject(app)
        deleteAlien(app)
        for i in app.objectSet:
            if isinstance(i, alien):
                i.moveAlien(app)
            else:
                i.rotateMoon(app)
        app.astro.rotateChar()
        if app.timePassed % 40 == 0 and app.inSpace:
            app.astro.gravityPull(app)
            app.astro.moveChar(app)
            app.astro.wrapChar(app)
            app.astro.rotateChar()
            createNewAlien(app)
            if app.astro.isCollision(app) != None:
                app.inSpace = False
                if app.astro.isCollision(app) == app.secondMoon:
                    temp = app.firstMoon
                    app.firstMoon = app.secondMoon
                    app.secondMoon = temp
                else:
                    # put game over stuff here!!!
                    pass
        elif app.timePassed % 30 == 0 and not app.inSpace:
            app.astro.orbitChar(app, app.firstMoon)

def redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2,
                        image = ImageTk.PhotoImage(app.background))
    for i in app.objectSet:
        i.drawObject(app, canvas)
    app.astro.drawChar(app, canvas)

runApp(width = 500, height = 800)