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
def Previtt():
    for i in range(2, width1):
        for j in range(2, height1):
            GradModx = (bright(i, j - 2) + bright(i, j - 1) + bright(i, j)) - (bright(i - 2, j - 2) + bright(i - 2, j) + bright(i - 2, j - 1))
            GradMody = (bright(i, j) + bright(i - 1, j) + bright(i - 2, j)) - (bright(i - 2, j - 2) + bright(i - 1, j - 2) + bright(i, j - 2))
            GradMod = sqrt(GradModx*GradModx + GradMody*GradMody)
            if GradMod > 280:
                previttMass.append([i - 1, j - 1])

def Drawing():
    Previtt()
    draww = ImageDraw.Draw(img1)
    for i in range(len(previttMass)):
        draww.point(previttMass[i], fill=ImageColor.getrgb("red"))
    img1.save("Previttequal.png", "PNG")

Drawing()
