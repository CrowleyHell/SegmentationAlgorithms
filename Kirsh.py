from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor

img1 = Image.open('equalNoize.png')
img1 = img1.convert('RGB')
width1, height1 = img1.size

def bright(x, y):
    rgbPix = img1.getpixel((x, y))
    r, g, b = rgbPix
    brightness = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
    return brightness


previttMass = []

L = [lambda x, y: (x - 2, y - 2),
     lambda x, y: (x - 1, y - 2),
     lambda x, y: (x, y - 2),
     lambda x, y: (x, y - 1),
     lambda x, y: (x, y),
     lambda x, y: (x - 1, y),
     lambda x, y: (x - 2, y),
     lambda x, y: (x - 2, y - 1)
     ]

def Kirsh():
    val = []
    for i in range(2, width1):
        for j in range(2, height1):
            for k in range(0, 7):
                S = bright(*L[(k + 0) % 8](i, j)) + bright(*L[(k + 1) % 8](i, j)) + bright(*L[(k + 2) % 8](i, j))
                T = bright(*L[(k + 3) % 8](i, j)) + bright(*L[(k + 4) % 8](i, j)) + bright(*L[(k + 5) % 8](i, j)) + \
                    bright(*L[(k + 6) % 8](i, j)) + bright(*L[(k + 7) % 8](i, j))
                val.append(abs(5*S - 3*T))
            maxVal = max(val)
            val = []
            finGrad = max(1, maxVal)
            if finGrad > 1300:
                previttMass.append((i, j))



def Drawing():
    Kirsh()
    draww = ImageDraw.Draw(img1)
    for i in range(len(previttMass)):
        draww.point(previttMass[i], fill=ImageColor.getrgb("red"))
    img1.save("kirshequal.png", "PNG")

Drawing()

