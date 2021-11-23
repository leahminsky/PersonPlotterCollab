class Line(object):
    def __init__(self, coords, color, size):
        self.coords = coords
        self.color = color 
        self.size = size

    def __repr__(self):
        return f"Color: {self.color}, Size: {self.size}, Coords:{self.coords}"

    def getCoords(self):
        return self.coords

    def addPoint(self, event):#turn this into just an add point method
        self.coords.append((event.x, event.y))

    def redraw(self, canvas):
        currLine = self.coords

        for i in range(1, len(currLine)):
            currPointX, currPointY = currLine[i]
            lastPointX, lastPointY = currLine[i-1]

            canvas.create_line(currPointX, currPointY, 
                    lastPointX, lastPointY, 
                    width = self.size, fill = self.color, smooth=True)


class Point(object):
    def __init__(self, coord, color, size):
        self.coord = coord
        self.color = color 
        self.size = size

    def __repr__(self):
        return f"Color: {self.color}, Size: {self.size}, Coords:{self.coord}"

    def getCoord(self):
        return self.coord

    def redraw(self, canvas):

        cx, cy = self.coord

        canvas.create_oval(cx - self.size/ 2, cy - self.size/2, 
                        cx + self.size/ 2, cy + self.size/2, 
                        fill = self.color)
