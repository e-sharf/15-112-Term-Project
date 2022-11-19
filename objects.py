# name: Ethan Sharf
# 15-112 Term Project

###############################################################################

# imports
import math
from cmu_112_graphics import *
from helpers import *

###############################################################################

class objects():
    def __init__(self):
        pass
    def randomSize(self):
        pass
    def randomPos(self):
        pass

class moon(objects):
    def __init__(self, cx, cy, radius):
        self.cx = cx
        self.cy = cy
        self.angle = 0
        self.r = radius
    def drawMoon(self, app, canvas):
        canvas.create_image(self.cx, self.cy,
                    image = ImageTk.PhotoImage(self.moon))
    # image from https://www.vectorstock.com/royalty-free-vector/
    # full-moon-cartoon-vector-4118531
    def createMoonImage(self, app):
        self.image = app.loadImage("moon_image.png")
        self.image = app.scaleImage(self.image, 1/self.r)
        self.moon = self.image
    def rotateMoon(self, app):
        self.angle += 5
        self.moon = self.image.rotate(self.angle, resample = Image.BILINEAR)
    def getImageCords(self):
        return(self.cx, self.cy)
    def getImageSize(self):
        imageWidth, imageHeight = self.moon.size
        return imageWidth, imageHeight
    def gravityRadius(self):
        return self.r*2
