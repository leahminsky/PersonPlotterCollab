import math, random 

def getAllxValues(originalLine):
    xValues = [ ]
    for coords in originalLine:
        xValues.append(coords[0])
    return xValues

def getAllyValues(originalLine):
    yValues = [ ]
    for coords in originalLine:
        yValues.append(coords[1])
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

# def isClosedShape(originalLine):
#     closedShape = False
#     startPoint = originalLine[0]
#     endPoint = originalLine[-1]
#     if (distanceHelper(startPoint, endPoint)< avgDistBtwnPoints(originalLine)):
#         closedShape = True
#     return closedShape

def pointEqualtoPoint(x, y, originalLine):
    for coord in originalLine:
        if (x, y) == coord:
            equal = True
    equal = False
    return equal

def touchingShape(originalLine):
    minX, minY, maxX, maxY = findBounds(originalLine)
    for row in range(minX, maxX):
        for col in range (minY, maxY):
            if  pointEqualtoPoint(row, col, originalLine):
                touchingShape = True

#maybe move these two into the response class?

# Used http://paulbourke.net/geometry/pointlineplane/ for calculating the 
#intersection points
def getIntersection(a1, a2, b1, b2):
    x1, y1 = a1
    x2, y2 = a2
    x3, y3 = b1
    x4, y4 = b2
    denom = ((x2-x1)*(y4-y3)-(y1-y2)*(x3-x4))

    #lines have to have more than 0 length
    if ((x1 == x2 and y1 == y2) or (x3==x4 and y3 == y4)):
        return  None 
    #parallel
    if (denom == 0):
        return  None 

    uA = ((x4-x3)*(y1-y3)-(y4-y3)*(x1-x3)) / denom
    uB = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)) / denom

    if (uA < 0 or uA > 1 or uB < 0 or uB > 1):
        return  None 

    x = x1 + uA * (x2 - x1)
    y = y1 + uA * (y2 - y1)
    return  (x, y) 



# def mirrorOverCenter(coord):
# #takes the line and mirrors it over the center of the canvas
#     x , y = coord[0], coord[1]
#     center = (canvasWidth/2)
#     distanceFromCenter = abs(x - center)#<--I think i need to do abs here?
#     newX = center + distanceFromCenter
#     return (newX, y)

# def jaggedScribble(originalLine):
#     minX, minY, maxX, maxY = findBounds(originalLine)
#     for i in range(len(originalLine)):
#         px = random.randint(minX, maxX)
#         py = random.randint(minY, maxY)
#         ad.lineTo(px, py)

# #golan's code, ported https://editor.p5js.org/golan/sketches/im4aJHJO_
# def scribblyLine(startX, startY):
#     goDirection = random.random(2*math.pi)
#     baseStepSize = 5
#     headingBias = 0.6
#     nIterations = 100 #<--size of originalList?
#     px = startX
#     py = startY
    
#     for i in range(nIterations):
#         stepSize = baseStepSize + (noise(i / 20.0 + 10) - 0.5)#<map to 0 and 1?
#         dx = px - startX
#         dy = py - startY
#         dh1 = max(0.0001, math.sqrt(dx * dx + dy * dy) / 250)
#         stepSize *= 1.0 - 0.9 * dh1

#         goDirection += math.radians(20.0 * (noise(i / 10.0) - headingBias))

#         px += stepSize * math.cos(goDirection)
#         py += stepSize * math.sin(goDirection)

#         dh1 = math.pow(dh1, -0.3)
#         qx = startX + dx * dh1
#         qy = startY + dy * dh1
#         ad.lineTo(qx, qy)

# def mapResponses(self):
#         responses = {
#             0: mirrorOverCenter,
#             1: scribblyLine,
#             2: jaggedScribble,
#             3: filledShape
#         }

class Response(object):
    def __init__(self, responseId, originalStroke):
        self.originalStroke = originalStroke
        # self.responseId = responseId
        self.responseId = 2
        self.alreadyDrawn = False

    def __repr__(self):
        return f"Id: {self.responseId}, Coords: {self.originalStroke}"

    def drawSquare(self, size):
        startX, startY = self.originalStroke
        squareCoords = [ (startX, startY), (startX+size, startY), 
                        (startX+size, startY+size), (startX, startY+size),
                        (startX, startY) ]
        return squareCoords
#########################################UPDATE##############################
    def drawCircle(self, size):
        startX, startY = self.originalStroke
        squareCoords = [ (startX, startY), (startX+size, startY), 
                        (startX+size, startY+size), (startX, startY+size),
                        (startX, startY) ]
        return squareCoords

    def drawTriangle(self, size):
        startX, startY = self.originalStroke
        squareCoords = [ (startX, startY), (startX+size, startY), 
                        (startX+size, startY+size), (startX, startY+size),
                        (startX, startY) ]
        return squareCoords
#############################################################################

    def doToAllCoords(self):
        #just shows mirroring
        return self.originalStroke

    def fillIntersections(self):
        intersections = [ ]
        newRow = [ ]
        total = len(self.originalStroke)
        endpt2 = total - 1
        minX, minY, maxX, maxY = findBounds(self.originalStroke)
        for x in range(minX, maxX):
            newRow = [ ]
            intersections.append(newRow)
            for y in range(minY, maxY):
                for endpt1 in range(self.originalStroke):
                    newRow.append(getIntersection(x, y, 
                    self.originalStroke[endpt1], self.originalStroke[endpt2]))
        return intersections


    # def jaggedScribble(self):
    #     minX, minY, maxX, maxY = self.findBounds()
    #     transformedList = [ ]
    #     for i in range(len(self.originalStroke)):
    #         px = random.randint(minX, maxX)
    #         py = random.randint(minY, maxY)
    #         transformedList.append((px, py))
    #     return transformedList