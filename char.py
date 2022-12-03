# name: Ethan Sharf
# 15-112 Term Project

###############################################################################

# imports
from helpers import *
from objects import *
import math
import time

###############################################################################

# defines character class
class char():
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.angle = 0
        self.ratioX = 0
        self.ratioY = 0

    # returns character position
    def getCharMid(self):
        return self.cx, self.cy

    # draws the character on screen
    def drawChar(self, app, canvas):
        canvas.create_image(self.cx, self.cy,
                    image = ImageTk.PhotoImage(self.char))
    # assigns character image to image from folder
    # image from https://www.123rf.com/photo_129268090_cute-cartoon-astronaut-
    # on-the-moon-on-a-space-background.html
    def createCharImage(self, app):
        self.image = app.loadImage("astronaut_image.png")
        self.image = app.scaleImage(self.image, 1/5)
        self.char = self.image

    # rotates character
    def rotateChar(self, app):
        self.angle += app.firstMoon.rotateSpeed

    # rotates character in relation to moon rotation
    def orbitChar(self, app, object):
        imageX, imageY = object.getImageCords()
        imageWidth, imageHeight = object.getImageSize()
        self.cx = imageX + imageHeight*math.cos(-(self.angle+90)/180*math.pi) / 1.5
        self.cy = imageY + imageHeight*math.sin(-(self.angle+90)/180*math.pi) / 1.5
        self.char = self.image.rotate(self.angle, resample = Image.BILINEAR)

    # determines character velocity in horizontal and vertical directions
    def moveChar(self, app):
        multiplyer = 15
        if self.cy <= app.height//2:
            self.cx += multiplyer * self.ratioX
        else:
            self.cx += multiplyer * self.ratioX
            self.cy += multiplyer * self.ratioY
        return multiplyer * self.ratioX, multiplyer * self.ratioY
         
    # determines if the character collides with any objects  
    def isCollision(self, app):
        for i in app.objectSet:
            objectX, objectY  = i.getImageCords()
            objectWidth, objectHeight = i.getImageSize()
            leftBound = objectX - objectWidth//2
            rightBound = objectWidth//2 + objectX
            topBound = objectY - objectHeight//2
            bottomBound = objectY + objectHeight//2
            if (leftBound <= self.cx <= rightBound and 
                topBound <= self.cy <= bottomBound):
                return i

    # allows for character to move off the screen horizontally and reappear on
    # the other side of the screen
    def wrapChar(self, app):
        if self.cx > app.width:
            self.cx = 0
        if self.cx < 0:
            self.cx = app.width

    # determines the vertical and horizontal factors for when character is in motion
    def createVector(self, object):
        imageX, imageY = object.getImageCords()
        self.ratioY = (self.cy - imageY) / (((self.cy -imageY)**2 + (self.cx - imageX)**2) **.5)
        self.ratioX = (self.cx - imageX) / (((self.cy -imageY)**2 + (self.cx - imageX)**2) **.5)

    # determines the gravitational pull on the character based on distance from object
    def gravityPull(self, app):
        for i in app.objectSet:
            noGravObject = isinstance(i, shield) or isinstance(i, alien)
            if time.time() - app.time0 > .2 and not noGravObject:
                x0, y0, x1, y1 = i.gravityRadius()
                if x0 <= self.cx <= x1 and y0 <= self.cy <= y1:
                    imageX, imageY = i.getImageCords()
                    self.ratioX -= (self.cx - imageX) / (((self.cy -imageY)**2 
                            + (self.cx - imageX)**2) **.8)
                    self.ratioY -= (self.cy - imageY) / (((self.cy -imageY)**2 
                            + (self.cx - imageX)**2) **.8)
    
    # checks if character is on screen vertically
    def boundsCheck(self, app):
        if self.cy > app.height:
            return True

    # toggles between red and normal image for a certain time
    def toggleImage(self, app):
        if not app.charToggle and time.time() - app.collisionTime <= 1.2:
            self.createCharImage(app)
            app.charToggle = not app.charToggle
        elif app.charToggle and time.time() - app.collisionTime <= 1.2:
            self.image = app.loadImage("astronaut_image_red.png")
            self.image = app.scaleImage(self.image, 1/5)
            self.char = self.image
            app.charToggle = not app.charToggle
        else:
            self.createCharImage(app)