# name: Ethan Sharf
# 15-112 Term Project

###############################################################################

# imports
import math
from cmu_112_graphics import *

###############################################################################

def getBounds(image, appWidth, appHeight, cx, cy):
    imageWidth, imageHeight = image.size
    imageWidth, imageHeight
    x0 = cx - imageWidth//2
    x1 = appWidth - cx + imageWidth//2
    y0 = cy - imageHeight//2
    y1 = appHeight - cy + imageHeight//2
    print((x0, y0, x1, y1))
    return (x0, y0, x1, y1)

# referenced https://www.geeksforgeeks.org/how-to-rotate-an-image-using-python/

def calculateAngle(app):
    pass


def moveInRotation(app):
    pass
    

def moveScreen():
    pass

def isCollision(app, item1, item2,):
    getBounds(item1, app.width, app.height, app.cx, app.cy)

def gravity():
    pass

def gravityPull():
    pass

def inBounds():
    pass