# name: Ethan Sharf
# 15-112 Term Project

###############################################################################

# imports
import math
from cmu_112_graphics import *
from helpers import *

###############################################################################

# defines superclass objects
class objects():
    # initializes objects
    def __init__(self, cx, cy, radius):
        self.cx = cx
        self.cy = cy
        self.r = radius
    
    # returns middle of image cordinates
    def getImageCords(self):
        return(self.cx, self.cy)
    
    # draws object based on image selected
    def drawObject(self, app, canvas):
        canvas.create_image(self.cx, self.cy,
                    image = ImageTk.PhotoImage(self.image))
    
    # determines if object is drawn within the radius of another
    def inRadius(self, app):
        for i in app.objectSet:
            if i is self or i is app.astro:
                continue
            else:
                x0, y0, x1, y1 = i.gravityRadius()
                if y0 <= self.cy <= y1:
                    return i
        return None
    
    # determines the radius in which the gravity reaches
    def gravityRadius(self):
        imageWidth, imageHeight = self.image.size
        return (self.cx - imageWidth*1.3, self.cy - imageHeight*1.3,
                self.cx + imageWidth*1.3, self.cy + imageHeight*1.3)
    
    # rotates object by 5 degrees
    def rotateObject(self, app):
        self.angle += 5
        self.image = self.tempImage.rotate(self.angle, resample = Image.BILINEAR)

################################################################################

# creates moon subclass
class moon(objects):
    # initizes objects
    def __init__(self, cx, cy, radius):
        super().__init__(cx, cy, radius)
        self.angle = 0
    
    # draws moon object from image in folder
    # image from https://www.vectorstock.com/royalty-free-vector/
    # full-moon-cartoon-vector-4118531
    def createMoonImage(self, app):
        self.tempImage = app.loadImage("moon_image.png")
        self.tempImage = app.scaleImage(self.tempImage, 1/self.r)
        self.image = self.tempImage

    # returns height and width of image
    def getImageSize(self):
        imageWidth, imageHeight = self.image.size
        return imageWidth, imageHeight

################################################################################

# creates blackHole subclass
class blackHole(objects):
    # initializes objects
    def __init__(self, cx, cy, radius):
        super().__init__(cx, cy, radius)
        self.angle = 0

    # draws black hole from image in folder
    # image from https://toppng.com/free-image/the-black-hole-in-space
    # -PNG-free-PNG-Images_1343
    def createHoleImage(self, app):
        self.tempImage = app.loadImage("black_hole_image.png")
        self.tempImage = app.scaleImage(self.tempImage, 1/self.r)
        self.image = self.tempImage

    # returns size of image
    def getImageSize(self):
        imageWidth, imageHeight = self.image.size
        return imageWidth, imageHeight

################################################################################

# creates alien subclass
class alien(objects):
    # initalizes objects
    def __init__(self, cx, cy, radius):
        super().__init__(cx, cy, radius)
        self.moveToggle = False
    
    # draws alien from image in folder
    # image from https://www.cleanpng.com/png-ufo-free-unidentified-flying
    # -object-flying-saucer-628381/preview.html
    def createUfoImage(self, app):
        self.newImage = app.loadImage("ufo_image.png")
        self.newImage = app.scaleImage(self.newImage, 1/self.r)
        self.image = self.newImage
    
    # returns image size
    def getImageSize(self):
        imageWidth, imageHeight = self.image.size
        return imageWidth, imageHeight
    
    # moves aliens horizontally
    def moveAlien(self, app):
        leftBound = app.width/6
        rightBound = 5*app.width/6 
        if self.cx > rightBound or self.cx < leftBound:
            self.moveToggle = not self.moveToggle
        if self.moveToggle:
            self.cx -= 5
        else:
            self.cx += 5          