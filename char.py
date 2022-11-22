# name: Ethan Sharf
# 15-112 Term Project

###############################################################################

# imports
import math
from helpers import *
from objects import *
import time

###############################################################################
class char():
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.angle = 0
        self.ratioX = 0
        self.ratioY = 0

    def getCharMid(self):
        return self.cx, self.cy

    def drawChar(self, app, canvas):
        canvas.create_image(self.cx, self.cy,
                    image = ImageTk.PhotoImage(self.char))

    # image from https://www.123rf.com/photo_129268090_cute-cartoon-astronaut-
    # on-the-moon-on-a-space-background.html
    def createCharImage(self, app):
        self.image = app.loadImage("astronaut_image.png")
        self.image = app.scaleImage(self.image, 1/5)
        self.char = self.image

    def rotateChar(self):
        self.angle += 5

    def orbitChar(self, app, object):
        imageX, imageY = object.getImageCords()
        imageWidth, imageHeight = object.getImageSize()
        self.cx = imageX + imageHeight*math.cos(-(self.angle+90)/180*math.pi) / 1.5
        self.cy = imageY + imageHeight*math.sin(-(self.angle+90)/180*math.pi) / 1.5
        self.char = self.image.rotate(self.angle, resample = Image.BILINEAR)

    def moveChar(self, app):
        if self.cy <= app.height//2:
            self.cx += 15 * self.ratioX
        else:
            self.cx += 15 * self.ratioX
            self.cy += 15 * self.ratioY
        return 15 * self.ratioY
         
    def isCollision(self, app):
        for i in app.objectSet:
            objectX, objectY  = i.getImageCords()
            objectWidth, objectHeight = i.getImageSize()
            leftBound = objectX - objectWidth//2
            rightBound = objectWidth//2 + objectX
            topBound = objectY - objectHeight//2
            bottomBound = objectY + objectHeight//2
            if leftBound <= self.cx <= rightBound and topBound <= self.cy <= bottomBound:
                return i

    def wrapChar(self, app):
        if self.cx > app.width:
            self.cx = 0
        if self.cx < 0:
            self.cx = app.width

    def createVector(self, object):
        imageX, imageY = object.getImageCords()
        self.ratioY = (self.cy - imageY) / (((self.cy -imageY)**2 + (self.cx - imageX)**2) **.5)
        self.ratioX = (self.cx - imageX) / (((self.cy -imageY)**2 + (self.cx - imageX)**2) **.5)
    
    def gravityPull(self, app):
        for i in app.objectSet:
            if time.time() - app.time0 > .2 and not isinstance(i, alien):
                x0, y0, x1, y1 = i.gravityRadius()
                if x0 <= self.cx <= x1 and y0 <= self.cy <= y1:
                    imageX, imageY = i.getImageCords()
                    self.ratioX -= (self.cx - imageX) / (((self.cy -imageY)**2 + (self.cx - imageX)**2) **.70)
                    self.ratioY -= (self.cy - imageY) / (((self.cy -imageY)**2 + (self.cx - imageX)**2) **.70)            