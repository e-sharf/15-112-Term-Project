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
    # creating background image
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
    app.screen = 0
    app.score = 0

    # screen images
    app.startAstro = app.loadImage("astronaut_image.png")
    app.startAstro = app.scaleImage(app.startAstro, 1/3)
    app.endAlien = app.loadImage("ufo_image.png")
    app.endAlien = app.scaleImage(app.endAlien, 1/3)

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

    # creating hole object
    app.hole = blackHole(app.width, app.height, 100)
    app.hole.createHoleImage(app)
    app.objectSet.add(app.hole)

def keyPressed(app, event):
    if event.key == "Up" and not app.inSpace:
        app.inSpace = True
        app.time0 = time.time()
        app.astro.createVector(app.firstMoon)
    if event.key == "r" or event.key == "R":
        appStarted(app)

def mousePressed(app, event):
    if (app.screen == 0 and app.width//4 <= event.x <= 3*app.width//4
        and 7*app.height//10 <= event.y <= 9*app.height//10):
        app.screen = 1

# creating new moons
def createNewMoons(app):
    charX1, charY1 = app.firstMoon.getImageCords()
    charX2, charY2 = app.secondMoon.getImageCords()
    spawnX = app.width * random.randint(30,70)/100
    spawnY = -240
    spawnR = random.randint(3, 5)
    if charY1 - app.height*.05 > app.height:
        app.objectSet.remove(app.firstMoon)
        app.firstMoon = moon(spawnX, spawnY, spawnR)
        if app.firstMoon.inRadius(app) != None:
            i = app.firstMoon.inRadius(app)
            app.objectSet.remove(i)
        app.firstMoon.createMoonImage(app)
        app.objectSet.add(app.firstMoon)
    if charY2 - app.height*.075 > app.height and scroll:
        app.objectSet.remove(app.secondMoon)
        app.secondMoon = moon(spawnX, spawnY, spawnR)
        if app.secondMoon.inRadius(app) != None:
            i = app.secondMoon.inRadius(app)
            app.objectSet.remove(i)
        app.secondMoon.createMoonImage(app)
        app.objectSet.add(app.secondMoon)

def createNewObject(app):
    num = random.randint(1, 100)
    if num <= 10:
        randX = random.randint(30,70)
        app.ufo = alien(app.width *  randX / 100, -100, 4)
        app.objectSet.add(app.ufo)
        if app.ufo.inRadius(app) == None:
            app.ufo.createUfoImage(app)
        else:
            app.objectSet.remove(app.ufo)
    elif num >= 90:
        randX = random.randint(30,70)
        # Used uniform to get floats from https://docs.python.org/3/library/random.html
        app.hole = blackHole(app.width *  randX / 100, -300, random.uniform(2.5, 4))
        app.objectSet.add(app.hole)
        if app.hole.inRadius(app) == None:
            app.hole.createHoleImage(app)
        else:
            app.objectSet.remove(app.hole)
        

def deleteObject(app):
    newSet = set()
    for i in app.objectSet:
        charX, charY = i.getImageCords()
        if (charY - app.height*.25) > app.height and (isinstance(i, alien) or isinstance(i, blackHole)):
            continue
        else:
            newSet.add(i)
    app.objectSet = newSet

def timerFired(app):
    if app.screen != 1:
        return
    app.timePassed += app.timerDelay
    if app.timePassed % 100 == 0:
        scoreCounter(app)
    if app.timePassed % 30 == 0:
        scroll(app)
        createNewMoons(app)
        deleteObject(app)
        app.astro.rotateChar()
        for i in app.objectSet:
            if isinstance(i, alien):
                i.moveAlien(app)
            else:
                i.rotateObject(app)
        if app.timePassed % 40 == 0 and app.inSpace:
            app.astro.gravityPull(app)
            app.astro.moveChar(app)
            app.astro.wrapChar(app)
            createNewObject(app)
            if app.astro.isCollision(app) != None:
                app.inSpace = False
                if app.astro.isCollision(app) == app.secondMoon:
                    temp = app.firstMoon
                    app.firstMoon = app.secondMoon
                    app.secondMoon = temp
                elif app.astro.isCollision(app) == app.firstMoon:
                    pass
                else:
                    # comment out to debug!!!
                    app.screen = 2
        elif app.timePassed % 30 == 0 and not app.inSpace:
            app.astro.orbitChar(app, app.firstMoon)

def redrawAll(app, canvas):
    if app.screen == 0:
        drawStart(app, canvas)
    if app.screen == 1:
        canvas.create_image(app.width//2, app.height//2,
                            image = ImageTk.PhotoImage(app.background))
        for i in app.objectSet:
            i.drawObject(app, canvas)
        app.astro.drawChar(app, canvas)
        canvas.create_text(20, 20, text = f'Score: {app.score}', anchor = "nw", 
                fill = "white", font = 'Helvetica 12')
    if app.screen == 2:
        drawGameOver(app, canvas)

runApp(width = 500, height = 800)