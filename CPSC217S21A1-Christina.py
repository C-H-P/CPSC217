# COURSE CPSC 231 SPRING 2021
# INSTRUCTOR: Jonathan Hudson
# XywaW4RTguuM0XLxXdlD
# UCID: 30168171
# Name: Christina He

"""
This program takes user's input for the position of the center of the sun and house.
Then the program will place the sun and the house in the pre-configured setting.
Suggested input for x and y coordinate of the moon(sun): (775,25)
Suggested input for x and y coordinate of the house: (140,140)
"""
from SimpleGraphics import *
# Constant
# Sun coordinates and size
sunCenterPositionX = int(input("Please enter the x coordinate of the center of the moon(sun): "))
sunCenterPositionY = int(input("Please enter the y coordinate of the center of the moon(sun): "))
sunDiameter = int(50)
sunLeftUpperPositionX = sunCenterPositionX - sunDiameter // 2
sunLeftUpperPositionY = sunCenterPositionY - sunDiameter // 2
# Window's dimensions (system)
windowDimensionX = int(800)
windowDimensionY = int(600)
# Road coordinates, four corners
roadBottomLeftX = int(0)
roadBottomLeftY = int(400)
roadUpperLeftX = int(0)
roadUpperLeftY = int(250)
roadBottomRightX = int(800)
roadBottomRightY = int(600)
roadUpperRightX = int(800)
roadUpperRightY = int(450)
# House body coordinates and dimension
houseCenterX = int(input("Please enter the x coordinate of the center of the house: "))
houseCenterY = int(input("Please enter the y coordinate of the center of the house: "))
houseDimension = int(200)
houseUpperLeftX = houseCenterX - houseDimension // 2
houseUpperLeftY = houseCenterY - houseDimension // 2
# Five points to create the pentagon part of the sign
signP1X = houseUpperLeftX + 1.5 * houseDimension
signP1Y = houseUpperLeftY + houseDimension//2 - 20
signP2X = signP1X + 10
signP2Y = signP1Y - 8
signP3X = signP2X + 35
signP3Y = signP2Y
signP4X = signP3X
signP4Y = signP1Y + 8
signP5X = signP2X
signP5Y = signP4Y
# Rectangle coordinates to create the bottom part of the sign
signBottomX = signP4X-10
signBottomY = signP4Y
signBottomLength = 10
signBottomWidth = 50
# Coordinates of the position of the door and the size of the door
doorLength = houseDimension // 4
doorWidth = houseDimension // 3
doorPositionX = houseUpperLeftX + houseDimension//2
doorPositionY = houseUpperLeftY + houseDimension - doorWidth
#Line to divide the main floor and the second floor of the house
houseSegmentX1 = houseUpperLeftX
houseSegmentY1 = houseUpperLeftY + houseDimension//2
houseSegmentX2 = houseUpperLeftX + houseDimension
houseSegmentY2 = houseSegmentY1
# Words on the sign
textPositionX = (signP2X + signP3X)//2
textPositionY = (signP2Y + signP5Y)//2
# Window's coordinates and dimensions (picture)
windowUpperLeftX = houseUpperLeftX + 5
windowUpperLeftY = houseUpperLeftY + 5
windowLength = houseDimension - 10
windowWidth = houseDimension // 2 - 10
# window frames
windowFrameHorizontalX1 = windowUpperLeftX
windowFrameHorizontalY1 = windowUpperLeftY + windowWidth // 2
windowFrameHorizontalX2 = windowUpperLeftX + windowLength
windowFrameHorizontalY2 = windowFrameHorizontalY1
windowFrameVerticalLeftX1 = windowUpperLeftX + windowLength // 4
windowFrameVerticalLeftY1 = windowUpperLeftY
windowFrameVerticalLeftX2 = windowFrameVerticalLeftX1
windowFrameVerticalLeftY2 = windowUpperLeftY + windowWidth
windowFrameVerticalRightX1 = windowUpperLeftX + windowLength // 4 * 3
windowFrameVerticalRightY1 = windowUpperLeftY
windowFrameVerticalRightX2 = windowFrameVerticalRightX1
windowFrameVerticalRightY2 = windowUpperLeftY + windowWidth
windowFrameVerticalMiddleX1 = windowUpperLeftX + windowLength // 4 * 2
windowFrameVerticalMiddleY1 = windowUpperLeftY
windowFrameVerticalMiddleX2 = windowFrameVerticalMiddleX1
windowFrameVerticalMiddleY2 = windowUpperLeftY + windowWidth
# roof
roofUpperLeftX = houseUpperLeftX
roofUpperLeftY = houseUpperLeftY - houseDimension // 4
roofUpperRightX = houseUpperLeftX + houseDimension
roofUpperRightY = roofUpperLeftY
roofLowerLeftX = houseUpperLeftX - houseDimension // 5
roofLowerLeftY = houseUpperLeftY
roofLowerRightX = houseUpperLeftX + houseDimension * 1.2
roofLowerRightY = roofLowerLeftY
# Haystacks position and size
haystackSize = int(50)
haystack1X = int(500)
haystack1Y = int(200)
haystack2X = haystack1X + haystackSize // 3
haystack2Y = haystack1Y + haystackSize // 12
haystack3X = haystack2X + haystackSize // 3
haystack3Y = haystack2Y + haystackSize // 12
haystack4X = haystack3X + haystackSize // 3
haystack4Y = haystack3Y + haystackSize // 12
haystack5X = haystack4X + haystackSize // 3
haystack5Y = haystack4Y + haystackSize // 12
# Draw landscape
# Setting up the window
resize(windowDimensionX,windowDimensionY)
background("dark blue")
# Road
setFill("black")
polygon(roadBottomRightX,roadUpperRightY,roadUpperRightX,roadBottomRightY,roadBottomLeftX,roadBottomLeftY,roadUpperLeftX,roadUpperLeftY)
setFill("black")
#Haystack
ellipse(haystack1X,haystack1Y,haystackSize,haystackSize)
ellipse(haystack2X,haystack2Y,haystackSize,haystackSize)
ellipse(haystack3X,haystack3Y,haystackSize,haystackSize)
ellipse(haystack4X,haystack4Y,haystackSize,haystackSize)
ellipse(haystack5X,haystack5Y,haystackSize,haystackSize)

# Draw Sun
setFill("khaki1")
ellipse(sunLeftUpperPositionX,sunLeftUpperPositionY,sunDiameter,sunDiameter)

# Draw house
# Body
setFill("bisque")
rect(houseUpperLeftX,houseUpperLeftY,houseDimension,houseDimension)
# Door
setFill("moccasin")
rect(doorPositionX,doorPositionY,doorLength,doorWidth)
# segment
line(houseSegmentX1,houseSegmentY1,houseSegmentX2,houseSegmentY2)
#Window
setFill("gold")
setOutline("saddle brown")
rect(windowUpperLeftX,windowUpperLeftY,windowLength,windowWidth)
# Horizontal middle frame
line(windowFrameHorizontalX1,windowFrameHorizontalY1,windowFrameHorizontalX2,windowFrameHorizontalY2)
# Vertical left frame
line(windowFrameVerticalLeftX1,windowFrameVerticalLeftY1,windowFrameVerticalLeftX2,windowFrameVerticalLeftY2)
# Vertical middle frame
line(windowFrameVerticalMiddleX1,windowFrameVerticalMiddleY1,windowFrameVerticalMiddleX2,windowFrameVerticalMiddleY2)
# Vertical right frame
line(windowFrameVerticalRightX1,windowFrameVerticalRightY1,windowFrameVerticalRightX2,windowFrameVerticalRightY2)
# Sign
setFill("saddle brown")
polygon(signP1X,signP1Y,signP2X,signP2Y,signP3X,signP3Y,signP4X,signP4Y,signP5X,signP5Y)
rect(signBottomX,signBottomY,signBottomLength,signBottomWidth)
setOutline("black")
setFont("Times", "10", "italic")
text(textPositionX, textPositionY, "Luna")
#Roof
setFill("burlywood1")
polygon(roofUpperLeftX,roofUpperLeftY,roofUpperRightX,roofUpperRightY,roofLowerRightX,roofLowerRightY,roofLowerLeftX,roofLowerLeftY)
