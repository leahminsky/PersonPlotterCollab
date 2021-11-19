#CANNOT RUN UNLESS CONNEECTED TO AXIDRAW

import sys

from cmu_112_graphics import *
from pyaxidraw import axidraw

#modeled off of https://axidraw.com/doc/py_api/#quick-start-interactive-xy
# ad = axidraw.AxiDraw()
# ad.interactive()                
# ad.options.model = 2                
# connected = ad.connect()         
# if not connected:
#     sys.exit

#ensures that it starts at home position
# ad.moveto(0, 0)
############################SIZE######################################
#based on aspect ratio of axidraw v3 model
canvasWidth = 880
canvasHeight = 680
mouseScaleFactor = 85
margin = 5
######################################################################
#make draw features into classes maybe? or maybe just make the main a class

#example of a dynamic gui element
class Button(object):
    def __init__(self, label, color, topLeftX, topLeftY):
        self.label = label
        self.color = color
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY

    def buttonLocation(self):
        return self.topLeftX, self.topLeftY

    def buttonSettings(self):
        text = self.label
        buttonWidth = len(text)*10 #find a ratio num so button size is dynamic
        buttonHeight = 20
        buttonColor = self.color
        return buttonWidth, buttonHeight, buttonColor

    def buttonOutline(self, outCol):
        buttonOutlineWidth = 5
        buttonOutlineColor = "blue"
        return buttonOutlineWidth, buttonOutlineColor

def inBounds(x, y):
    if (x > 0 and x < (canvasWidth-margin) and y > 0 
                        and y < (canvasHeight-margin)):
        return True
    return False

def appStarted(app):
    app.mouseDrag = False
    app.mousePress = False

    app.x1, app.y1 = 0, 0
    app.x2, app.y2 = 0, 0

    app.linePos = [ ]
    app.num = len(app.linePos)

    #making button ex.
    app.zigZagButton = Button("Zig Zag Line", "green", 10, 10)

def keyPressed(app, event):
    if event.key == 'h': #moves to origin
        # ad.moveto(0, 0)
        pass

def mousePressed(app, event):
    app.mousePress = True
    if inBounds(event.x, event.y): 
        app.linePos.append((event.x, event.y))
        print(app.linePos)
        app.x1, app.y1 = app.linePos[0]
        app.x2, app.y2 = app.linePos[0]
        # ad.pendown()

        #need to make functionality for when a button is clicked it changes 
        #the drawing tool to that feature
        # if (zigZagButtonSelected):
        #     ad.lineto((newX)/mouseScaleFactor, (newY)/mouseScaleFactor) 
# import math
# class Coordinate(object):
#     def __init__(self, x,y):
#         self.x = x
#         self.y = self

#     def __repr__(self):
#         return f"{self.x} + , {self.y}"

#     def angle(self):
#         return math.atan2(self.y, self.x)

def perpindicular(coord):
    #calculate perp

def mouseReleased(app, event):
    app.mousePress = False
    # ad.penup()

def mouseMoved(app, event):
    # app.mouseDrag = False
    if inBounds(event.x, event.y): 
        # ad.moveto((event.x)/mouseScaleFactor, (event.y)/mouseScaleFactor)
        pass

def mouseDragged(app, event):
    newX, newY = 0, 0
    zigZag = 0
    app.mouseDrag = True
    if inBounds(event.x,event.y):
        app.linePos.append((event.x, event.y))
        for i in range(1, len(app.linePos)):
                app.linePos[i] = app.linePos[i-1]
                # newX, newY = drawFeature1(app.linePos[i], zigZag) 
        # ad.lineto((event.x)/mouseScaleFactor, (event.y)/mouseScaleFactor)
        
def drawFeature1(curr, zigZag):
    #zigzag line, this is just an example not gonna actually use
    currX, currY = curr[0], curr[1]
    if (zigZag == 0):
        currX, currY
        zigZag = 1
        zigZagX = currX + 20
    else:
        zigZag = 0
        zigZagY = currY + 20

    return zigZagX, zigZagY

#at the moment I cannot figure out why my drawing line is not 
#appearing on the canvas
def redrawAll(app, canvas):
    x, y = app.zigZagButton.buttonLocation()
    width, height, col = app.zigZagButton.buttonSettings()
    outlineWidth, outlineCol = app.zigZagButton.buttonOutline("pink")
    canvas.create_rectangle(x, y, width, height, fill = col, 
                    outline = outlineCol, width = outlineWidth)
    # print(app.mouseDrag, app.mousePress)
    # if (app.mouseDrag):
    for i in range(1, len(app.linePos)-1):
        canvas.create_line(app.linePos[i][0], app.linePos[i][1], 
                app.linePos[i-1][0], app.linePos[i-1][1], 
                width = 5, fill = "black")
# elif (app.mousePress):
    canvas.create_line(app.x1, app.y1, app.x2, app.y2, 
                        width = 5, fill = "black")

def runAxi():
    runApp(width = canvasWidth, height = canvasHeight)

runAxi()
# ad.moveto(0,0)      #moves back to origin before closing app
# ad.disconnect() 
