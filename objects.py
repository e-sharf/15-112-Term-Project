# name: Ethan Sharf
# 15-112 Term Project

###############################################################################

# imports
import math
from cmu_112_graphics import *
from helpers import *

###############################################################################

class objects():
    def __init__(self,):
        pass
    def randomSize(self):
        pass
    def randomPos(self):
        pass

class moon(objects):
    def __init__(self, cx, cy, radius):
        self.cx = cx
        self.cy = cy
        self.moonAngle = 0
        self.r = radius
    def drawMoon(self, app, canvas):
        canvas.create_image(self.cx, self.cy,
                    image = ImageTk.PhotoImage(self.moonRotate))
    def createMoonImage(self, app):
        # image from https://www.vectorstock.com/royalty-free-vector/
        # full-moon-cartoon-vector-4118531
        self.image = app.loadImage("moon_image.png")
        self.image = app.scaleImage(self.image, 1/3)
        self.moon = self.image
        self.moonRotate = self.moon
    def rotateMoon(self, app):
        app.timePassed += app.timerDelay
        imageWidth, imageHeight = getImageSize(self.moon, self.cx, self.cy)
        if app.timePassed >= 200:
            self.moonAngle += 5
            self.moonRotate = self.moon.rotate(self.moonAngle, resample = Image.BILINEAR)
            app.charX = self.cx + imageHeight*math.cos(-(self.moonAngle+90)/180*math.pi) // 2
            app.charY = self.cy + imageHeight*math.sin(-(self.moonAngle+90)/180*math.pi) // 2
            app.charRotate = app.astronaut.rotate(self.moonAngle, 
                        resample = Image.BILINEAR)
            app.timePassed = 0
