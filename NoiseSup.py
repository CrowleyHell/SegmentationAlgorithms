from PIL import Image

img = Image.open('equal.png')
img = img.convert('RGB')
width, height = img.size


def noiseSup():
    for i in range(1, width):
        for j in range(1, height):
            rgbLeftUp = img.getpixel((i - 1, j - 1))
            rgbRightDown = img.getpixel((i, j))
            rgbLeftDown = img.getpixel((i - 1, j))
            rgbRightUp = img.getpixel((i, j - 1))
            r, g, b = rgbLeftUp
            r1, g1, b1 = rgbLeftDown
            r2, g2, b2 = rgbRightUp
            r3, g3, b3 = rgbRightDown
            midrefR = int((r + r1 + r2 + r3)/4)
            midrefG = int((g + g1 + g2 + g3)/4)
            midrefB = int((b + b1 + b2 + b3)/4)
            if r > midrefR and g > midrefG and b > midrefB:
                img.putpixel((i - 1, j - 1), (midrefR, midrefG, midrefB))
noiseSup()

img.save('equalNoize.png', 'PNG')