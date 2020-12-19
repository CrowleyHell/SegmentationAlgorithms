import cv2 as cv

image = cv.imread('equalNoize.png', 1)
Gaussian = cv.GaussianBlur(image, (3, 3), 0)
cv.imwrite('equalGauss2.png', Gaussian)