# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
image = cv2.imread('110928.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
filename = "{}.jpg".format(os.getpid())
cv2.imwrite(filename, gray)
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)


cv2.imshow("Image", image)
cv2.imshow("Output", gray)

