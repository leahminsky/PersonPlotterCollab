class Line(object):
    def __init__(self, coords, color, size):
        #add a boolean flag for if already drawn, draw if it is false
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

class Square(object):
    def __init__(self, coord, color, size):
        self.coord = coord
        self.color = color 
        self.size = size

    def __repr__(self):
        return f"Color: {self.color}, Size: {self.size}, Coord:{self.coord}"

    def getCoord(self):
        return self.coord 

    def redraw(self, canvas):

        cx, cy = self.coord

        canvas.create_rectangle(cx, cy, 
                        cx + self.size, cy + self.size, outline = self.color,
                        width = 8)

class Circle(object):
    def __init__(self, coord, color, size):
        self.coord = coord
        self.color = color 
        self.size = size

    def __repr__(self):
        return f"Color: {self.color}, Size: {self.size}, Coord:{self.coord}"

    def getCoord(self):
        return self.coord 

    def redraw(self, canvas):

        cx, cy = self.coord

        canvas.create_oval(cx, cy, 
                        cx + self.size, cy + self.size, outline = self.color,
                        width = 8)

class Triangle(object):
    def __init__(self, coord, color, size):
        self.coord = coord
        self.color = color 
        self.size = size

    def __repr__(self):
        return f"Color: {self.color}, Size: {self.size}, Coord:{self.coord}"

    def getCoord(self):
        return self.coord 

    def redraw(self, canvas):

        cx, cy = self.coord

        #make a bool flag that tracks if there have been 3 mouse presses,
        #if so, get thouse past three mouse positions stored in some list
        #and send those to this triangle class
        canvas.create_polygon(cx, cy, 
                        cx + self.size, cy + self.size, outline = self.color,
                        width = 8)
