from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
from math import *

img = Image.open('equalGauss2.png')
img = img.convert('RGB')
width, height = img.size
previttMass = []


def bright(x, y):
    rgbPix = img.getpixel((x, y))
    r, g, b = rgbPix
    brightness = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
    return brightness


def Grad():
    for i in range(2, width):
        for j in range(2, height):
            Gradx = (bright(i, j - 2) + bright(i, j - 1) + bright(i, j)) - (
                        bright(i - 2, j - 2) + bright(i - 2, j) + bright(i - 2, j - 1))
            Grady = (bright(i, j) + bright(i - 1, j) + bright(i - 2, j)) - (
                        bright(i - 2, j - 2) + bright(i - 1, j - 2) + bright(i, j - 2))
            GradMod = sqrt(Gradx*Gradx + Grady*Grady)
            previttMass.append((i, j, GradMod))


nmsMass = []
def NMS():
    for i in range(2, len(previttMass)):
        if previttMass[i - 1][2] > previttMass[i - 2][2] and previttMass[i - 1][2] > previttMass[i][2]:
            nmsMass.append((previttMass[i - 1][0], previttMass[i - 1][1], previttMass[i - 1][2]))

finalMass = []
def Canny():
    Grad()
    NMS()
    for i in range(2, len(nmsMass)):
        if nmsMass[i - 1][2] > 70:
            finalMass.append((nmsMass[i - 1][0], nmsMass[i - 1][1], nmsMass[i - 1][2]))
        elif nmsMass[i - 1][2] < 20 and nmsMass[i - 2][2] > 70 and nmsMass[i][2] > 70:
            finalMass.append((nmsMass[i - 1][0], nmsMass[i - 1][1], nmsMass[i - 1][2]))

def Drawing():
    Canny()
    draww = ImageDraw.Draw(img)
    for i in range(len(finalMass)):
        draww.point((finalMass[i][0], finalMass[i][1]), fill=ImageColor.getrgb("red"))
    img.save("cannyequal222.png", "PNG")

Drawing()
