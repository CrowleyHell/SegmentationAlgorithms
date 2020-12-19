from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor


img = Image.open('equalNoize.png')
img = img.convert('RGB')
width, height = img.size
mass = []





def bright(x, y):
    rgbPix = img.getpixel((x, y))
    r, g, b = rgbPix
    brightness = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
    return brightness


previttMass = []
def Laplas():
    curLap = True
    basicLap = True
    for i in range(1, width):
        for j in range(1, height):
            laplas = 8*bright(i - 1, j - 1) - (bright(i - 2, j - 2) + bright(i - 1, j - 2) + bright(i, j - 2) +
                                                    bright(i, j - 1) + bright(i, j) + bright(i - 1, j) +
                                                    bright(i - 2, j) + bright(i - 2, j - 1))
            if laplas < 0:
                curLap = False
            elif laplas > 0: curLap = True
            if curLap != basicLap:
                previttMass.append([i - 1, j - 1])
                basicLap = curLap



def Drawing():
    Laplas()
    draww = ImageDraw.Draw(img)
    for i in range(len(previttMass)):
        draww.point(previttMass[i], fill=ImageColor.getrgb("red"))
    img.save("Laplasequal.png", "PNG")

Drawing()
