################# BUILT IN MODULES #################

import os, sys, random, math

###################################################

from stroke import *
from responses import *

#################### MODULES ######################

from cmu_112_graphics import *
from pyaxidraw import axidraw

#################################################

canvasWidth = 880
canvasHeight = 680
mouseScaleFactor = 85
margin = 5


#intialize axidraw for interactive mode
ad = axidraw.AxiDraw()
ad.interactive()                
ad.options.model = 2               
connected = ad.connect()         
if not connected:
    print(axidraw is not connected)
    sys.exit

#################### INITIAL WAIT SCREEN ######################

# def splashScreenMode_redrawAll(app, canvas):
#     axiReady = False
#     if (axiReady):
#         canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill="red")
#         canvas.create_text(app.width/2, 150, text="Aligning plotter...", 
#                                                             fill="white")
# #         os.system("axicli -m align")
#         ad.penup()
#         ad.moveto(0,0)
#         axiReady = True
# #         print("pen in up position")
# #         print("motors unlocked")
# #         print("pen in home position")
#     else:
#         cX = canvasWidth/2
#         cY = canvasHeight/2
#         canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill="white")
#         canvas.create_rectangle(cX-20, cY+20, cX-20, cY+20, fill="green")
#         canvas.create_text(app.width/2, 150, text="Start!", 
#                                                         fill="white")
# def splashScreenMode_buttonBounds(x, y):
#     cX = canvasWidth/2
#     cY = canvasHeight/2
#     if (x > cX-20 and x < cX+20 and y < cY-20 and y > cY+20):
#         inBounds = True
#     inBounds = False
#     return inBounds

# def splashScreenMode_mousePressed(app, event):
#     startApp = False
#     if splashScreenMode_buttonBounds(event.x, event.y):
#         app.mode = ""

#################### DRAW MODE SCREEN ######################

def inBounds(x, y):
    if (x > 0 and x < (canvasWidth-margin) and y > 0 
                        and y < (canvasHeight-margin)):
        return True
    return False

def inButton(x, y):
    if (x > canvasWidth-50 and x < 50 and y > canvasWidth-20 
                        and y < 20):
        return True
    return False

def constrainResponseLine(newList):
    mouseScaleFactor = 85
    constrainedResponse = [ ]
    for coord in newList:
        x = coord[0] / mouseScaleFactor
        y = coord[1] / mouseScaleFactor
        constrainedResponse.append((x, y))
    return constrainedResponse

def constrainResponsePoint(newPoint):
    mouseScaleFactor = 85
    x = newPoint[0] / mouseScaleFactor
    y = newPoint[1] / mouseScaleFactor
    return x, y

##################################################################

def getAllxValues(originalLine):
    xValues = [ ]
    for coords in originalLine:
        xValues.append(originalLine[coords[0]])
    return xValues

def getAllyValues(originalLine):
    yValues = [ ]
    for coords in originalLine:
        yValues.append(originalLine[coords[1]])
    return yValues

def findBounds(originalLine):
    #find min x and y, find max x and y
    minX = min(getAllxValues(originalLine))
    minY = min(getAllyValues(originalLine))
    maxX = max(getAllxValues(originalLine))
    maxY = max(getAllyValues(originalLine))
    return minX, minY, maxX, maxY

def distanceHelper(lastPoint, currPoint):
    x1, y1 = lastPoint #do i have to do lastPoint[0], lastPoint[1]?
    x2, y2 = currPoint #do i have to do currPoint[0], currPoint[1]?
    return math.sqrt( ((x1-x2)**2)+((y1-y2)**2) )

def avgDistBtwnPoints(originalLine):
    oldAvg = 0
    currAvg = 0
    bestAvg = 0
    for i in range(len(originalLine)):
        currPoint = originalLine[i]
        lastPoint = originalLine[i-1]
        currAvg = distanceHelper(lastPoint, currPoint)
        bestAvg = (currAvg + oldAvg) / 2
        oldAvg = currAvg
    return bestAvg

def isClosedShape(originalLine):
    closedShape = False
    startPoint = originalLine[0]
    endPoint = originalLine[-1]
    if  (distanceHelper(startPoint, endPoint) < 
                                avgDistBtwnPoints(originalLine)):
        closedShape = True
    return closedShape

###############################################################################

def randResponse():
    # responseIds = 2 #this will be passed in later
    # numResponses = len(responseIds)
    randNum = random.random()
    if (randNum < 0.5):
        return 0
    return 2

#  def changeShapeSize():
#     #inherits slider from gui
#     sizeValue = getSliderValue()
#     return sizeValue
    

def appStarted(app):
    # app.mode = 'splashScreenMode'

    app.strokes = [ ]
    app.newResponse = None
    app.transformed = [ ]
    app.alreadyDrawn = False

    app.userIsDrawing= False
    app.firstMove = True
    app.lineDrawn = False

    app.makeSquare = False
    app.dottedLine = False

    

#################### MOUSE EVENTS #######################

def mousePressed(app, event):
    # app.userIsDrawing = True

    if inBounds(event.x,event.y):
        if(app.makeSquare):
            newSquare = Square(coord=[event.x, event.y], color="black",
                                                    size=10)
            app.strokes.append(newSquare)
            app.makeSquare = False
        else:
            newPoint = Point(coord=[event.x, event.y], color="black", size=8)
            app.strokes.append(newPoint)

    app.userIsDrawing = True
    
def mouseReleased(app, event):
    app.userIsDrawing = False
    app.firstMove = True
    if not app.userIsDrawing and app.firstMove:
        if isinstance(app.strokes[-1], Line):
            if (isClosedShape(app.strokes[-1].getCoords())):
                app.newResponse = Response(1, app.strokes[-1].getCoords())
                app.transformed = app.newResponse.fillIntersections()
            else:
                app.newResponse = Response(randResponse(), 
                                                app.strokes[-1].getCoords())
                app.transformed = app.newResponse.doToAllCoords()

            app.transformed = constrainResponseLine(app.transformed)
            firstX, firstY = app.transformed[0]

        elif isinstance(app.strokes[-1], Square):
            app.newResponse = Response(0, app.strokes[-1].getCoord())
            app.transformed = app.newResponse.drawSquare(50)
            app.transformed = constrainResponseLine(app.transformed)
            firstX, firstY = app.transformed[0]
        else:
            app.newResponse = Response(0, app.strokes[-1].getCoord())
            app.transformed = app.newResponse.doToAllCoords()
            app.transformed = constrainResponsePoint(app.transformed)
            firstX, firstY = app.transformed
        ad.moveto(firstX, firstY)
        app.firstMove = False


def mouseDragged(app, event):   
    if app.userIsDrawing:
        if (len(app.strokes) == 0 or not isinstance(app.strokes[-1], Line)):
            # create new line
            newLine = Line(coords=[(event.x, event.y)], color="black", 
                size=4)
            app.strokes.append(newLine)

        else:
            # strokes exists
            lastStroke = app.strokes[-1]
            
            # add points
            if inBounds(event.x,event.y):
                lastStroke.addPoint(event)

def keyPressed(app, event):
    if event.key == 'e':
        ad.penup()
        ad.moveto(0,0)      #moves back to origin before closing app
        ad.disconnect()

    if event.key == 's':
        app.makeSquare = True
    

def doResponse(app):
    if not app.userIsDrawing:
        if not app.firstMove:
            if (app.newResponse.alreadyDrawn == False):
                ad.pendown()
                if isinstance(app.strokes[-1], Line):

                    if (app.newResponse.responseId == 1):
                        #fill shape
                        rows,cols=len(app.transformed),len(app.transformed[0])
                        for row in range(rows):
                            draw = False #substitute with moveto
                            count = 0
                            for col in range(cols):
                                if (isinstance(app.transformed[row][col], 
                                                                    tuple)):
                                    count+=1
                                    if (count % 2 == 0):
                                        draw = False #substitute with moveto
                                    draw = True #substitute with lineto

                    if (app.newResponse.responseId == 2):
                        #dash line
                        for coord in range(len(app.transformed)):
                            if coord == (len(app.transformed)):
                                app.newResponse.alreadyDrawn = True
                            else:
                                if (coord % 2 != 0):
                                    x, y = app.transformed[coord]
                                    ad.moveto(x, y)
                                else:
                                    x, y = app.transformed[coord]
                                    ad.lineto(x, y)

                    if (app.newResponse.responseId == 0):
                        #mirror
                        for coord in range(len(app.transformed)):
                            if coord == len(app.transformed):
                                ad.penup()
                                continue
                            x, y = app.transformed[coord]
                            ad.lineto(x, y)
                            
                    app.newResponse.alreadyDrawn = True
                    ad.penup()

                elif isinstance(app.strokes[-1], Square):
                    for coord in range(len(app.transformed)):
                        if coord == len(app.transformed):
                            ad.penup()
                            continue
                        x, y = app.transformed[coord]
                        ad.lineto(x, y)
                        app.newResponse.alreadyDrawn = True
                else:
                    x, y = app.transformed
                    ad.lineto(x, y)
        

        
############################################################################
# responseIds = {
#             0: mirror,
#             1: filledShape,
#             2: dashedLine,
#             3: scribblyLine,
#             4: jaggedScribble,
#         }
# def randNum(responseIds):
#     numResponses = len(responseIds)
#     randNum = random.randint(0, numResponses)
#     return randNum

############################################################################

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill="#daf0e6")
    canvas.create_text(app.width/2, 20, text="e to exit, s for square", 
                                                            fill="green")

    for drawStroke in app.strokes:
        drawStroke.redraw(canvas)

    doResponse(app)

def runAxi():
    runApp(width = canvasWidth, height = canvasHeight)

runAxi()

ad.penup()
ad.moveto(0,0)      #moves back to origin before closing app
ad.disconnect()






