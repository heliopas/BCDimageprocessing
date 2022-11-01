from imutils.perspective import four_point_transform
import cv2
import pytesseract
import imutils
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\RompkoH\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('rdm6591Gray.png')

#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#ref, img = cv2.threshold(img, 53, 255, cv2.THRESH_BINARY, cv2.THRESH_OTSU)

img = imutils.resize(img, height=250)
gray = cv2.bilateralFilter(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 11, 17, 17)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
ref, img = cv2.threshold(img, 54, 255, cv2.THRESH_BINARY, cv2.THRESH_OTSU)
edged = cv2.Canny(gray, 30, 200)


print(pytesseract.image_to_string(img))
cv2.imshow('Result', img)

cv2.waitKey(0)