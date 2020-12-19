import cv2 as cv
import numpy as np

img = cv.imread('test.png', 1)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

l, a, b = cv.split(lab)


clahe = cv.createCLAHE(clipLimit=40.0, tileGridSize=(8,8))
cl = clahe.apply(l)

limg = cv.merge((cl, a, b))

final = cv.cvtColor(limg, cv.COLOR_LAB2BGR)
res = np.hstack((img, final)) #stacking images side-by-side

cv.imwrite('CLAHE.png', res)