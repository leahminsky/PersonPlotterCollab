#CANNOT RUN UNLESS CONNEECTED TO AXIDRAW

import sys, math

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


def inBounds(x, y):
    if (x > 0 and x < (canvasWidth-margin) and y > 0 
                        and y < (canvasHeight-margin)):
        return True
    return False

def constrain(x, y):
    constrainedX = x/mouseScaleFactor
    constrainedY = y/mouseScaleFactor
    return constrainedX, constrainedY


def appStarted(app):
    app.mouseDrag = False
    app.mousePress = False
    app.userJustWent = False

    app.lines = [ ]
    # app.currLine = [ ]
    app.numLines = len(app.lines)
    

def keyPressed(app, event):
    if event.key == 'h':
        # ad.penUp() #lift pen then move to origin
        # ad.moveto(0, 0)
        pass

def mousePressed(app, event):
    app.mousePress = True
    app.mouseDrag = False
    currLine = [ ]
    if inBounds(event.x, event.y):
        app.lines.append(currLine)
        currLine.append((event.x, event.y))
        app.userJustWent = True

        # ad.pendown()

def mouseReleased(app, event):
    app.mousePress = False
    app.mouseDrag = False
    app.userJustWent = True
    
    #change the pen speed when axidraw needs to cover a large surface area?
    #like in golan's example
    # ad.penup()

def mouseMoved(app, event):
    # app.mouseDrag = False
    if inBounds(event.x, event.y): 
        # ad.moveto((event.x)/mouseScaleFactor, (event.y)/mouseScaleFactor)
        pass


def mouseDragged(app, event):
    app.mousePress = False
    app.mouseDrag = True
    app.userJustWent = True

    currLine = [ ]
    if inBounds(event.x,event.y):
        if (len(currLine) > 0):
            currLine.append((event.x, event.y))
        else: #or object?
            app.lines.append(currLine)
            currLine.append((event.x, event.y))
        

def userDraw(app, canvas):
    currLine = app.lines[app.numLines]

    if (app.mouseDrag):
        for i in range(app.numLines):
            currLine = app.lines[i]
            for j in range(1, len(currLine)):
                currPointX, currPointY = currLine[j]
                lastPointX, lastPointY = currLine[j-1]

                canvas.create_line(currPointX, currPointY, 
                        lastPointX, lastPointY, 
                        width = 5, fill = "black", smooth="true")
                        
                currPointX, currPointY = lastPointX, lastPointY

    if (app.mousePress):
        for i in range(app.numLines):
            currLine = app.lines[i]
            currPointX, currPointY = currLine[i][0]
        
            canvas.create_oval(currPointX, currPointY, 
                            currPointX+2, currPointY+2, 
                            fill = "black")

def robotDraw(app, canvas):
    currLine = app.lines[app.numLines]
    numLinePoints = len(currLine)

    #### debug view ########### 
    for i in range(numLinePoints):
        currPoint = currLine[i]
        lastPoint = currLine[i-1]
        currPointX, currPointY = (currPoint[0]+10, currPoint[1] - 20)
        lastPointX, lastPointY = (lastPoint[0]+10, lastPoint[1] - 20)
        canvas.create_line(currPointX, currPointY, 
                        lastPointX, lastPointY, 
                        width = 5, fill = "red", smooth="true")
        
        currPoint = lastPoint
    ##############

    # if (numLinePoints > 0):
    #     desiredAxiPoint = currLine[numLinePoints]
    #     moveAxiHere(desiredAxiPoint)
        #ad.lineto(desiredAxiPoint.x, desiredAxiPoint.y)

def moveAxiHere(goPoint):
    mX, mY = constrain(goPoint[0], goPoint[1])
    return mX, mY
    # ad.moveTo(mX, mY)


def redrawAll(app, canvas):
    print(app.lines)
    if (app.mouseDrag):
        userDraw(app, canvas)
    elif (app.mousePress):
        userDraw(app, canvas)
    elif (app.userJustWent and not app.mouseDrag and not app.mousePress):
        robotDraw(app, canvas)
    else:
        #do nothing
        # ad.penUp()
        pass

def runAxi():
    runApp(width = canvasWidth, height = canvasHeight)

runAxi()
# ad.moveto(0,0)      #moves back to origin before closing app
# ad.disconnect() 
