# name: Ethan Sharf
# 15-112 Term Project

###############################################################################

# imports
from cmu_112_graphics import *
import math
import time

###############################################################################

# top scrolls based on position of character and if inSpace
def scroll(app):
    charX, charY = app.astro.getCharMid()
    moonX, moonY = app.firstMoon.getImageCords()
    charVeloX, charVeloY = app.astro.moveChar(app)
    if charY <= app.height/2 and charVeloY > 0:
        app.astro.cx += charVeloX
        app.astro.cy += charVeloY
    elif charY <= app.height/2:
        for i in app.objectSet:
            i.cy -= charVeloY
    if not app.inSpace and moonY <= 4*app.height/5:
        for i in app.objectSet:
            i.cy += 10

# draws start screen
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

# draws game over screen
def drawGameOver(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "grey")
    canvas.create_image(app.width//2, 3*app.height//5, image = ImageTk.PhotoImage(app.endAlien))
    canvas.create_image(app.width//2, 7*app.height//10, image = ImageTk.PhotoImage(app.startAstro))
    canvas.create_text(app.width//2, 2*app.height//5, 
            text = f'Game Over!\n Your Score is: {app.score}\nPress "r" to restart',
            fill = 'black', font = 'Helvetica 20', justify = 'center')

# draws main game screen
def drawGameScreen(app, canvas):
    canvas.create_image(app.width//2, app.height//2,
                        image = ImageTk.PhotoImage(app.background))
    for i in app.objectSet:
        i.drawObject(app, canvas)
    app.astro.drawChar(app, canvas)
    canvas.create_text(20, 20, text = f'Score: {app.score}', anchor = "nw", 
            fill = "white", font = 'Helvetica 12')
    for i in range(app.lives):
        x = 20 + 20*i
        y = 60
        canvas.create_image(x, y, image = ImageTk.PhotoImage(app.heart))

# calculates score
def scoreCounter(app):
    if app.inSpace:
        app.score += 50
    if not app.inSpace:
        if app.score <= 0:
            pass
        else:
            app.score -= 10

# determines closest moon to character
def closerMoon(app):
    charX, charY = app.astro.getCharMid()
    firstMoonX, firstMoonY = app.firstMoon.getImageCords()
    secondMoonX, secondMoonY = app.secondMoon.getImageCords()
    dis1 = ((charX - firstMoonX)**2 + (charY - firstMoonY)**2)**.5
    dis2 = ((charX - secondMoonX)**2 + (charY - secondMoonY)**2)**.5
    if dis1 < dis2:
        return app.firstMoon
    else:
        return app.secondMoon

# when running into an enemy decrease lives by one and put character on closest planet
def enemyCollision(app):
    app.collisionTime = time.time()
    app.lives -= 1
    if app.lives < 0:
        app.screen = 2
    else:
        if closerMoon(app) == app.firstMoon:
            pass
        else:
            temp = app.firstMoon
            app.firstMoon = closerMoon(app)
            app.secondMoon = temp

# changes firstMoon to secondMoon and secondMoon to firstMoon
def reassignMoon(app):
    temp = app.firstMoon
    app.firstMoon = app.secondMoon
    app.secondMoon = temp 