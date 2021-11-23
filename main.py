################# BUILT IN MODULES #################

import os, sys, random, math

###################################################

from stroke import *
from responses import *

#################### MODULES ######################

from cmu_112_graphics import *
from pyaxidraw import axidraw

#################################################

#modes --> first screen physically moves axidraw to origin, waiting screen 
#until ready to go
canvasWidth = 880
canvasHeight = 680
mouseScaleFactor = 85
margin = 5


#intialize axidraw for interactive mode
ad = axidraw.AxiDraw()
ad.interactive()                
ad.options.model = 2
# 
# should i do this when i align the axidraw in the waiting screen?                
connected = ad.connect()         
if not connected:
    print(axidraw is not connected)
    sys.exit

ad.penup()

#################### INITIAL WAIT SCREEN ######################

# def intitialWaitScreenMode_redrawAll(app, canvas):
#     makeBackground(color, width, height, etc)
#     makeButton("start")
# #maybe don't need this screen?

# def initialWaitScreenMode_mousePressed(app, event):
#     if button.mousePressed()?

# while(mode=="home screen"):
#     makeBackground(color, width, height, etc)
#     button = makeButton("start")
#     if (mousePressed and within button):
#         mode = "waiting screen"

######################################################

# def intitialWaitScreenMode_redrawAll(app, canvas):
#     makeBackground(color, width, height, etc)
#     makeButton("start")

# def intitialWaitScreenMode_redrawAll(app, canvas):
#     while(mode == "waiting screen" and not axiReady):
#         makeBackground(color, width, height, etc)
#         screenMessage = "Aligning plotter..."
#         axiReady = False
#         os.system("axicli -m align")
#         print("motors unlocked")
#         ad.penup()
#         print("pen in up position")
#         ad.moveto(0,0)
#         print("pen in home position")
#         axiReady = True
#         if (axiReady):
#             screenMessage = "Plotter is ready!"
#             #show "Go!" button 
#             if (mousePressed and in goButton):
#                 mode = "drawing app"

def inBounds(x, y):
    if (x > 0 and x < (canvasWidth-margin) and y > 0 
                        and y < (canvasHeight-margin)):
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

#function for checking what lines are already there?update actual canvas 
#with lines instead of just drawing over?

def appStarted(app):

    app.strokes = [ ]
    app.newResponse = None
    app.transformed = [ ]

    app.userIsDrawing= False
    app.firstMove = True
    app.lineDrawn = False

    

#################### MOUSE EVENTS #######################

def mousePressed(app, event):
    # app.userIsDrawing = True

    if inBounds(event.x,event.y):
        newPoint = Point(coord=[event.x, event.y], color="black", size=8)
    app.strokes.append(newPoint)

    app.userIsDrawing = True
    
def mouseReleased(app, event):
    app.userIsDrawing = False
    app.firstMove = True
    if not app.userIsDrawing and app.firstMove:

        if isinstance(app.strokes[-1], Line):
            app.newResponse = Response(1, app.strokes[-1].getCoords())
            app.transformed = app.newResponse.doToAllCoords()
            app.transformed = constrainResponseLine(app.transformed)
            firstX, firstY = app.transformed[0]
            # ad.moveto(firstX, firstY)
        else:
            app.newResponse = Response(1, app.strokes[-1].getCoord())
            app.transformed = app.newResponse.doToAllCoords()
            app.transformed = constrainResponsePoint(app.transformed)
            firstX, firstY = app.transformed
        #print((firstX, firstY))
        ad.moveto(firstX, firstY)
        app.firstMove = False
    #possible switch bool flag here for userisdrawing


def mouseDragged(app, event):
    # print(event.x)    
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
    if event.key == 'h':
        ad.penup()
        ad.moveto(0,0)      #moves back to origin before closing app
        ad.disconnect()

def doResponse(app):
    if not app.userIsDrawing:
        if not app.firstMove:
            ad.pendown()
            if isinstance(app.strokes[-1], Line):
                for coord in range(len(app.transformed)):
                    if coord == len(app.transformed)-1:
                        ad.penup()
                        app.lineDrawn = True
                        continue
                    x, y = app.transformed[coord]
                    ad.lineto(x, y)
                    app.lineDrawn = False
            else:
                x, y = app.transformed
                ad.lineto(x, y)
                app.lineDrawn = True

def doResponseOnce(app):
    if (not app.lineDrawn):
        doResponse(app)
        


############################################################################
#import responses as response and then do 
# def listResponses(response):
#     listOfResponses = [ ]
#     for response in range(len(responses)):
#         listOfResponses.append("response." + responses[response])
#     return listOfResponses

# for i in range(0, len(responses)):
#     currResponse = random.choice(listOfResponses(response))

# #OR

# responseIds = {
#             0: mirrorOverCenter,
#             1: diffGrowth,
#             2: scribblyLine,
#             3: jaggedScribble,
#             4: filledShape
#         }
# #change this, it was first meant for if responseIds was a list
# def randNum(responseIds):
#     numResponses = len(responseIds)
#     randNum = random.randint(0, numResponses)
#     return randNum

# def randomResponse(responses):
#     shuffledList = random.shuffle(responses)
#     currResponse = shuffledList[randNum(responses)]
#     return currResponse

############################################################################

def redrawAll(app, canvas):
    # print(app.strokes)
    # print(app.mouseDrag, app.mousePress)

    for drawStroke in app.strokes:
        drawStroke.redraw(canvas)

def runAxi():
    runApp(width = canvasWidth, height = canvasHeight)

runAxi()

ad.penup()
ad.moveto(0,0)      #moves back to origin before closing app
ad.disconnect()






