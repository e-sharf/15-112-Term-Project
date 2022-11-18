# name: Ethan Sharf
# 15-112 Term Project

###############################################################################

# imports
import math
from helpers import *

###############################################################################
class char():
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.angle = 0
        self.ratioX = 0
        self.ratioY = 0

    def drawChar(self, app, canvas):
        canvas.create_image(self.cx, self.cy,
                    image = ImageTk.PhotoImage(self.char))

    def createCharImage(self, app):
        # image from https://www.123rf.com/photo_129268090_cute-cartoon-astronaut-
        # on-the-moon-on-a-space-background.html
        self.image = app.loadImage("astronaut_image.png")
        self.image = app.scaleImage(self.image, 1/5)
        self.char = self.image

    def rotateChar(self):
        self.angle += 5

    def orbitChar(self,app,object):
        imageX, imageY = object.getImageCords()
        imageWidth, imageHeight = object.getImageSize()
        self.cx = imageX + imageHeight*math.cos(-(self.angle+90)/180*math.pi) / 1.5
        self.cy = imageY + imageHeight*math.sin(-(self.angle+90)/180*math.pi) / 1.5
        self.char = self.image.rotate(self.angle, resample = Image.BILINEAR)

    def moveChar(self):
        self.cx += 10 * self.ratioX
        self.cy += 10 * self.ratioY

    def isCollision(self, app):
        for i in app.objectSet:
            objectX, objectY  = i.getImageCords()
            objectWidth, objectHeight = i.getImageSize()
            leftBound = objectX - objectWidth//2
            rightBound = objectWidth//2 + objectX
            topBound = objectY - objectHeight//2
            bottomBound = objectY + objectHeight//2
            if leftBound <= self.cx <= rightBound and topBound <= self.cy <= bottomBound:
                return True

    def wrapChar(self, app):
        if self.cx > app.width:
            self.cx = 0
        if self.cx < 0:
            self.cx = app.width

    def createVector(self, app, object):
        imageX, imageY = object.getImageCords()
        self.ratioY = (self.cy - imageY) / (((self.cy -imageY)**2 + (self.cx - imageX)**2) **.5)
        self.ratioX = (self.cx - imageX) / (((self.cy -imageY)**2 + (self.cx - imageX)**2) **.5)