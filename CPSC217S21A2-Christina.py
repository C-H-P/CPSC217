# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 271 summer 2021
# INSTRUCTOR: Jonathan Hudson
# v7BcNHlYhsYGCjEvaZrO
# DO NOT EDIT THE ABOVE LINES
# Christina He
# UCID: 30168171
# I'm doing the bonus part

from SimpleGraphics import *
# CONSTANTS AND VARIABLES
# window size
WIDTH = 800
HEIGHT = 800

# Axis
coordinateCenterX = WIDTH / 2
coordinateCenterY = HEIGHT / 2
xAxisStartX = coordinateCenterX - 300
xAxisStartY = coordinateCenterY
xAxisEndX = coordinateCenterX + 300
xAxisEndY = xAxisStartY
yAxisStartX = coordinateCenterX
yAxisStartY = coordinateCenterY - 300
yAxisEndX = yAxisStartX
yAxisEndY = coordinateCenterY + 300

# labels: tick mark and text label
xAxisLabelX = coordinateCenterX - 300
yAxisLabelY = coordinateCenterY - 300
xAxisTickMarkStartY = xAxisStartY - 5
xAxisTickMarkEndY = xAxisStartY + 5
yAxisTickMarkStartX = yAxisStartX - 5
yAxisTickMarkEndX = yAxisStartX + 5
xAxisTextLabelY = xAxisTickMarkEndY
yAxisTextLabelX = yAxisTickMarkEndX
labelOffset = 600 / 8
label = -1.0
numberOfLabels = 9

# calculation and count constants
colorChangingCount = 0
magnification = (300 / 4) / 0.25

# set default for variables to keep track of largest and smallest x and y in the constellation
# and track to see when to initialize the first set of values to compare the coordinates

# Setup window
resize(WIDTH, HEIGHT)
background("black")
print("This program draws constellations based on user-driven input")

# Draw axes
setOutline("blue")
line(xAxisStartX, xAxisStartY, xAxisEndX, xAxisEndY)
line(yAxisStartX, yAxisStartY, yAxisEndX, yAxisEndY)

# Add tick marks and labels
for labelCount in range(numberOfLabels):

    # Tick marks on x axis
    line(xAxisLabelX, xAxisTickMarkStartY, xAxisLabelX, xAxisTickMarkEndY)
    line(yAxisTickMarkStartX, yAxisLabelY, yAxisTickMarkEndX, yAxisLabelY)

    # Adding number labels under and beside axis
    setFont("Times", 10)
    if label != 0:
        text(xAxisLabelX, xAxisTextLabelY, label, "n")
        text(yAxisTextLabelX, yAxisLabelY, -label, "w")
    xAxisLabelX += labelOffset
    yAxisLabelY += labelOffset
    label += 0.25

# Draw constellations
# Get first input
count = int(input("Input count of constellation stars (<=0 to exit):"))

# Loop to draw constellations
while count > 0:
    setOutline("white")

    # x and y tracker for box initialization
    largestX = 0
    largestY = 0
    smallestX = 0
    smallestY = 0
    firstRound = True

    # Loop to draw stars
    for number in range(count):

        # Get inputs
        starXCoordinate = float(input("Please enter the x coordinate of your star:"))
        starYCoordinate = float(input("Please enter the y coordinate of your star:"))
        magnitude = float(input("Please enter the magnitude of your star:"))

        # Calculations
        size = 10 / (magnitude + 2)
        starXCoordinateCenter = coordinateCenterX + starXCoordinate * magnification - size / 2
        starYCoordinateCenter = coordinateCenterY - starYCoordinate * magnification - size / 2
        size = float("%3f" % size)
        starXCoordinateCenter = float("%3f" % starXCoordinateCenter)
        starYCoordinateCenter = float("%3f" % starYCoordinateCenter)

        # Output
        # Drawing stars
        ellipse(starXCoordinateCenter, starYCoordinateCenter, size, size)

        # Tracking largest and smallest x and y in stars
        if firstRound:
            largestX = starXCoordinateCenter
            largestY = starYCoordinateCenter
            smallestX = starXCoordinateCenter
            smallestY = starYCoordinateCenter
            firstRound = False
        if starXCoordinateCenter > largestX:
            largestX = starXCoordinateCenter
        if starXCoordinateCenter < smallestX:
            smallestX = starXCoordinateCenter
        if starYCoordinateCenter > largestY:
            largestY = starYCoordinateCenter
        if starYCoordinateCenter < smallestY:
            smallestY = starYCoordinateCenter

    # Edges
    # Get input
    edges = int(input("Please enter the number of edges you would like to draw:"))

    # Loop to draw the edges
    for edge in range(edges):
        # Changing color.
        if colorChangingCount % 3 == 0:
            setOutline("red")
        elif colorChangingCount % 3 == 1:
            setOutline("green")
        else:
            setOutline("yellow")

        # Take inputs for edges
        startEdgeX = float(input("Please enter the x coordinate of the start of the edge:"))
        startEdgeY = float(input("Please enter the y coordinate of the start of the edge:"))
        endEdgeX = float(input("Please enter the x coordinate of the end of the edge:"))
        endEdgeY = float(input("Please enter the y coordinate of the end of the edge:"))

        # Calculations
        startEdgeX = coordinateCenterX + startEdgeX * magnification
        startEdgeY = coordinateCenterY - startEdgeY * magnification
        endEdgeX = coordinateCenterX + endEdgeX * magnification
        endEdgeY = coordinateCenterY - endEdgeY * magnification

        # Drawing edges
        line(startEdgeX, startEdgeY, endEdgeX, endEdgeY)

        # Track largest and smallest x and y coordinate of the edges
        if startEdgeX > largestX:
            largestX = startEdgeX
        if endEdgeX > largestX:
            largestX = endEdgeX
        if startEdgeX < smallestX:
            smallestX = startEdgeX
        if endEdgeX < smallestX:
            smallestX = endEdgeX
        if startEdgeY > largestY:
            largestY = startEdgeY
        if endEdgeY > largestY:
            largestY = endEdgeY
        if startEdgeY < smallestY:
            smallestY = startEdgeY
        if endEdgeY < smallestY:
            smallestY = endEdgeY

    # box settings and calculations
    padding = 15
    lineLeftUpperX = smallestX-padding
    lineLeftUpperY = smallestY-padding
    lineLeftBottomX = lineLeftUpperX
    lineLeftBottomY = largestY + padding
    lineRightUpperX = largestX + padding
    lineRightUpperY = lineLeftUpperY
    lineRightBottomX = lineRightUpperX
    lineRightBottomY = lineLeftBottomY

    # Change color and print boxes
    setOutline("white")
    line(lineLeftUpperX, lineLeftUpperY, lineLeftBottomX, lineLeftBottomY)
    line(lineLeftBottomX, lineLeftBottomY, lineRightBottomX, lineRightBottomY)
    line(lineRightBottomX, lineRightBottomY, lineRightUpperX, lineRightUpperY)
    line(lineRightUpperX, lineRightUpperY, lineLeftUpperX, lineLeftUpperY)

    # Name setting
    name = input("Please enter the name of your constellation:")
    nameX = smallestX + (largestX - smallestX)/2
    nameY = smallestY + 3
    text(nameX, nameY, name)

    # color tracker increment
    colorChangingCount += 1

    # re-prompt
    count = int(input("Input count of constellation stars (<=0 to exit):"))


print("Drawing is complete!")
