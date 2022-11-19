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

class moon(objects):
    def __init__(self, cx, cy, radius):
        super().__init__(cx, cy, radius)
        self.angle = 0
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
    def getImageSize(self):
        imageWidth, imageHeight = self.moon.size
        return imageWidth, imageHeight
    def gravityRadius(self):
        imageWidth, imageHeight = self.moon.size
        return (self.cx - imageWidth*1.2, self.cy - imageHeight*1.2,
                self.cx + imageWidth*1.2, self.cy + imageHeight*1.2)