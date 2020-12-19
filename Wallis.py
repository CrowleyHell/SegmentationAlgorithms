from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
from math import *


img1 = Image.open('equalNoize.png')
img1 = img1.convert('RGB')
width1, height1 = img1.size

def bright(x, y):
    rgbPix = img1.getpixel((x, y))
    r, g, b = rgbPix
    brightness = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
    return brightness


previttMass = []
def Wallis():
    for i in range(2, width1):
        for j in range(2, height1):
            if bright(i - 1, j - 1) > 0 and bright(i - 1, j - 2) and bright(i, j - 1) and bright(i - 1, j) and bright(i - 2, j - 1):
                GradMod = log(bright(i - 1, j - 1)) - (1/4)*(log(bright(i - 1, j - 2)) + log(bright(i, j - 1)) +
                                                         log(bright(i - 1, j)) + log(bright(i - 2, j - 1)))
                if GradMod > 0.15:
                    previttMass.append((i - 1, j - 1))


def Drawing():
    Wallis()
    draww = ImageDraw.Draw(img1)
    for i in range(len(previttMass)):
        draww.point(previttMass[i], fill=ImageColor.getrgb("red"))
    img1.save("wallisequal.png", "PNG")

Drawing()
