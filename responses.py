import math, random 

# def mirrorOverCenter(coord):
# #takes the line and mirrors it over the center of the canvas
#     x , y = coord[0], coord[1]
#     center = (canvasWidth/2)
#     distanceFromCenter = abs(x - center)#<--I think i need to do abs here?
#     newX = center + distanceFromCenter
#     return (newX, y)

# def getAllxValues(originalLine):
#     xValues = [ ]
#     for coords in originalLine:
#         xValues.append(originalLine[coords[0]])
#     return xValues

# def getAllyValues(originalLine):
#     yValues = [ ]
#     for coords in originalLine:
#         yValues.append(originalLine[coords[1]])
#     return yValues

# def findBounds(originalLine):
#     #find min x and y, find max x and y
#     minX = min(getAllxValues(originalLine))
#     minY = min(getAllyValues(originalLine))
#     maxX = max(getAllxValues(originalLine))
#     maxY = max(getAllyValues(originalLine))
#     return minX, minY, maxX, maxY

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
    

# def diffGrowth():
#     pass



# def pattern():
#     pass

# def floodFill():
#     #choose starting position
#     #8 directions 
#     d = [(-1, -1),  (0, -1), (1, -1),
#          (-1, 0),   (0, 0),  (1, 0),
#          (-1, 1),   (0, 1),  (1, 1)]
#     #
#     pass

# def filledShape():
#     pass

# def mapResponses(self):
#         responses = {
#             0: mirrorOverCenter,
#             1: diffGrowth,
#             2: scribblyLine,
#             3: jaggedScribble,
#             4: filledShape
#         }

#OR I GUESS I CAN DO newList = [(function(coord) for coord in originalList)]
# class PointResponse(object):
#     def __init__(self, responseId, originalStroke ):
#         self.originalStroke = originalStroke
#         self.id = responseId

#     def __repr__(self):
#         return f"Color: {self.color}, Size: {self.size}, Coords:{self.coords}"

#     def doToAllCoords(self):
#         #placeholder, just shows mirroring
#         return self.originalStroke

class Response(object):
    def __init__(self, responseId, originalStroke ):
        self.originalStroke = originalStroke
        self.responseId = responseId

    def __repr__(self):
        return f"Id: {self.responseId}, Coords: {self.originalStroke}"

    # def doToAllCoords(self):
    #     newStroke = [ ]
    #     for coord in self.originalStroke:
    #         newCoord = self.responsesId(coord)
    #         newStroke.append(newCoord)
    #     return newStroke

    def doToAllCoords(self):
        #placeholder, just shows mirroring
        return self.originalStroke
        #no this is just returning original stroke OBJECT, return actual list


    # def constrainResponse(newList):
    #     mouseScaleFactor = 85
    #     constrainedResponse = [ ]
    #     for coord in newList:
    #         x = coord[0] / mouseScaleFactor
    #         y = coord[1] / mouseScaleFactor
    #         constrainedResponse.append(x, y)
    #     return constrainedResponse

    # def goToFirstPoint(self):
    #     desiredAxiPointX, desiredAxiPointY = self.originalStroke[-1]

    # def redraw(self):
    #     desiredAxiPointX, desiredAxiPointY = self.originalStroke[-1]

    #     return desiredAxiPointX, desiredAxiPointY

            # canvas.create_line(currPointX, currPointY, 
            #         lastPointX, lastPointY, 
            #         width = self.size, fill = self.color, smooth=True)
