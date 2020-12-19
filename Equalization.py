import cv2 as cv
import numpy as np

img = cv.imread('test.png', 0)
equ = cv.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv.imwrite('equal1.png', res)