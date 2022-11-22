# name: Ethan Sharf
# 15-112 Term Project

###############################################################################

# imports
from cmu_112_graphics import *
import math
import time

###############################################################################

def getBounds(app, image, cx, cy):
    imageWidth, imageHeight = image.size
    imageWidth, imageHeight
    x0 = cx - imageWidth//2
    x1 = app.width - cx + imageWidth//2
    y0 = cy - imageHeight//2
    y1 = app.height - cy + imageHeight//2
    return (x0, y0, x1, y1)

def scroll(app):
    charX, charY = app.astro.getCharMid()
    moonX, moonY = app.firstMoon.getImageCords()
    charVeloY = app.astro.moveChar(app)
    if charY <= app.height/2 and charVeloY < 0:
        for i in app.objectSet:
            i.cy -= charVeloY
    if not app.inSpace and moonY <= 4*app.height/5:
        for i in app.objectSet:
            i.cy += 10

def drawStart(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "grey")
    canvas.create_text(app.width//2, app.height//5, text='Sticky Space',
                       fill='black', font='Helvetica 26 bold ')
    # learned how to use justify. https://www.tutorialspoint.com/how-do-i-center
    # -the-text-in-a-tkinter-text-widget#:~:text=To%20configure
    # %20and%20align%20the,can%20use%20justify%3DCENTER%20property.
    canvas.create_text(app.width//2, 3*app.height//5, text = 'Welcome to Sticky Space by Ethan Sharf!\n'
            'You control an astronaut who manipulates gravity\nand jumps from planet to planet '
            'while avoiding\nobstacles such as black holes and aliens. '
            'To jump\nfrom a planet pressed the up arrow but be sure to your\njump with '
            'the rotation of the planet\nGood Luck!', justify = "center", fill='black', font='Helvetica 12')
    canvas.create_rectangle(app.width//4, 7*app.height//10, 3*app.width//4, 9*app.height//10, fill = 'red')
    canvas.create_text(app.width//2, 4*app.height//5, text = "Press Here to Start!",
            fill = 'black', font = 'Helvetica 18 bold')
    canvas.create_image(app.width//2, 2*app.height//5, image = ImageTk.PhotoImage(app.startAstro))

def drawGameOver(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "grey")
    canvas.create_image(app.width//2, 3*app.height//5, image = ImageTk.PhotoImage(app.endAlien))
    canvas.create_image(app.width//2, 7*app.height//10, image = ImageTk.PhotoImage(app.startAstro))
    canvas.create_text(app.width//2, 2*app.height//5, 
            text = f'Game Over!\n Your Score is: {app.score}\nPress "r" to restart',
            fill = 'black', font = 'Helvetica 20', justify = 'center')

def scoreCounter(app):
    if app.inSpace:
        app.score += 50
    if not app.inSpace:
        if app.score <= 0:
            pass
        else:
            app.score -= 10
