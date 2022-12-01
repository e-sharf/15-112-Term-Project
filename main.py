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
    app.collisionTime = 0
    app.screen = 0
    app.score = 0
    app.lives = 3
    app.charToggle = False

    # screen images
    # image from https://www.123rf.com/photo_129268090_cute-cartoon-astronaut-
    # on-the-moon-on-a-space-background.html
    app.startAstro = app.loadImage("astronaut_image.png")
    app.startAstro = app.scaleImage(app.startAstro, 1/3)
    # image from https://www.cleanpng.com/png-ufo-free-unidentified-flying
    # -object-flying-saucer-628381/preview.html
    app.endAlien = app.loadImage("ufo_image.png")
    app.endAlien = app.scaleImage(app.endAlien, 1/3)
    # image from https://www.pngwing.com/en/free-png-invqg
    app.heart = app.loadImage("heart_image.png")
    app.heart = app.scaleImage(app.heart, 1/32)

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

# creates new moons
def createNewMoons(app):
    charX1, charY1 = app.firstMoon.getImageCords()
    charX2, charY2 = app.secondMoon.getImageCords()
    spawnX = app.width * random.randint(30,70)/100
    spawnY = -290
    spawnR = random.randint(3, 5)
    # if firstMoon goes off screen, remove it from the set and spawn in a new moon
    if charY1 - app.height*.02 > app.height:
        app.objectSet.remove(app.firstMoon)
        app.firstMoon = moon(spawnX, spawnY, spawnR)
        if app.firstMoon.inRadius(app) != None:
            i = app.firstMoon.inRadius(app)
            app.objectSet.remove(i)
        app.firstMoon.createMoonImage(app)
        app.objectSet.add(app.firstMoon)
    # if secondMoon goes off screen, remove it from the set and spawn in a new moon
    if charY2 - app.height*.02 > app.height and scroll:
        app.objectSet.remove(app.secondMoon)
        app.secondMoon = moon(spawnX, spawnY, spawnR)
        if app.secondMoon.inRadius(app) != None:
            i = app.secondMoon.inRadius(app)
            app.objectSet.remove(i)
        app.secondMoon.createMoonImage(app)
        app.objectSet.add(app.secondMoon)

# creates new black hole and alien objects
def createNewObject(app):
    num = random.randint(1, 100)
    # creates new alien object
    if num <= 12:
        randX = random.randint(30,70)
        app.ufo = alien(app.width *  randX / 100, -100, 4)
        app.objectSet.add(app.ufo)
        if app.ufo.inRadius(app) == None:
            app.ufo.createUfoImage(app)
        else:
            app.objectSet.remove(app.ufo)
    # creates new black hole object
    elif num >= 88:
        randX = random.randint(30,70)
        # Used uniform to get floats. learned from https://docs.python.org/3/library/random.html
        app.hole = blackHole(app.width *  randX / 100, -300, random.uniform(2.5, 4))
        app.objectSet.add(app.hole)
        if app.hole.inRadius(app) == None:
            app.hole.createHoleImage(app)
        else:
            app.objectSet.remove(app.hole)
        
# removes objects that collide when spawned in
def deleteObject(app):
    newSet = set()
    for i in app.objectSet:
        charX, charY = i.getImageCords()
        if ((charY - app.height*.25) > app.height and
         (isinstance(i, alien) or isinstance(i, blackHole))):
            continue
        else:
            newSet.add(i)
    app.objectSet = newSet

def timerFired(app):
    if app.screen != 1:
        return
    app.timePassed += app.timerDelay
    # counts score
    if app.timePassed % 100 == 0:
        scoreCounter(app)
    if app.timePassed % 30 == 0:
        app.astro.rotateChar()
        # triggers lost life animation
        if time.time() - app.collisionTime <= 2:
            app.astro.toggleImage(app)
        scroll(app)
        createNewMoons(app)
        deleteObject(app)
        # checks if char is off bottom of screen
        if app.astro.boundsCheck(app):
            app.screen = 2
        # moves aliens or rotates moon or black hole
        for i in app.objectSet:
            if isinstance(i, alien):
                i.moveAlien(app)
            else:
                i.rotateObject(app)
        # triggers if char is not on planet.
        # moves char by vector, pulls if in gravity radius, and wraps char if off side of screen
        if app.timePassed % 40 == 0 and app.inSpace:
            app.astro.gravityPull(app)
            app.astro.moveChar(app)
            app.astro.wrapChar(app)
            createNewObject(app)
            # checking collision with char
            if app.astro.isCollision(app) != None:
                app.inSpace = False
                if app.astro.isCollision(app) == app.secondMoon:
                    reassignMoon(app)
                elif app.astro.isCollision(app) == app.firstMoon: 
                    pass
                else:
                    enemyCollision(app)
        elif app.timePassed % 30 == 0 and not app.inSpace:
            app.astro.orbitChar(app, app.firstMoon)

def redrawAll(app, canvas):
    if app.screen == 0:
        drawStart(app, canvas)
    if app.screen == 1:
        drawGameScreen(app, canvas)
    if app.screen == 2:
        drawGameOver(app, canvas)

runApp(width = 500, height = 800)