# name: Ethan Sharf
# 15-112 Term Project

###############################################################################

# imports
import math
from cmu_112_graphics import *
from helpers import *

###############################################################################

class objects():
    def __init__(self, cx, cy, radius):
        self.cx = cx
        self.cy = cy
        self.r = radius
    def getImageCords(self):
        return(self.cx, self.cy)
    def drawObject(self, app, canvas):
        canvas.create_image(self.cx, self.cy,
                    image = ImageTk.PhotoImage(self.image))
    def inRadius(self, app):
        for i in app.objectSet:
            if i is self or i is app.astro:
                continue
            else:
                x0, y0, x1, y1 = i.gravityRadius()
                if y0 <= self.cy <= y1:
                    return i
        return None
    def gravityRadius(self):
        imageWidth, imageHeight = self.image.size
        return (self.cx - imageWidth*1.2, self.cy - imageHeight*1.2,
                self.cx + imageWidth*1.2, self.cy + imageHeight*1.2)

class moon(objects):
    def __init__(self, cx, cy, radius):
        super().__init__(cx, cy, radius)
        self.angle = 0
    # image from https://www.vectorstock.com/royalty-free-vector/
    # full-moon-cartoon-vector-4118531
    def createMoonImage(self, app):
        self.moon = app.loadImage("moon_image.png")
        self.moon = app.scaleImage(self.moon, 1/self.r)
        self.image = self.moon
    def rotateMoon(self, app):
        self.angle += 5
        self.image = self.moon.rotate(self.angle, resample = Image.BILINEAR)
    def getImageSize(self):
        imageWidth, imageHeight = self.image.size
        return imageWidth, imageHeight

class alien(objects):
    def __init__(self, cx, cy, radius):
        super().__init__(cx, cy, radius)
        self.moveToggle = False
    # image from https://www.cleanpng.com/png-ufo-free-unidentified-flying
    # -object-flying-saucer-628381/preview.html
    def createUfoImage(self, app):
        self.newImage = app.loadImage("ufo_image.png")
        self.newImage = app.scaleImage(self.newImage, 1/self.r)
        self.image = self.newImage
    def getImageSize(self):
        imageWidth, imageHeight = self.image.size
        return imageWidth, imageHeight
    def moveAlien(self, app):
        leftBound = app.width/6
        rightBound = 5*app.width/6 
        if self.cx > rightBound or self.cx < leftBound:
            self.moveToggle = not self.moveToggle
        if self.moveToggle:
            self.cx -= 5
        else:
            self.cx += 5          