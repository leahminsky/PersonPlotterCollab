# PersonPlotterCollab

**Drawing With a Machine**

This project allows you to collaboratively draw with a robot, more specifically, a pen plotter. When you draw something on the app, the plotter will respond in some unexpected, altered way in the robot’s own antagonistic “style” that contributes to the drawing you are creating together. There will be several drawing features that allow for different variations of response on the plotter’s side.

**Dependencies**

AxiDraw by Evil Mad Scientist, Python CLI (https://axidraw.com/doc/py_api/#)

**How To Run Project**

1. Download the project
2. Connect AxiDraw to computer
3. To make sure motors are are unlocked, in terminal type:
```
$ python axicli -m align
```
3. Physically move AxiDraw to home position (0, 0) if not already there
4. In terminal type:
```
$ python /path/to/folder/main.py
```
**Video**

Link goes here

**Controls**

Simply draw with your mouse on the canvas in draw mode. 
Do not draw while the plotter is taking its turn, you must wait until it's turn is over.


