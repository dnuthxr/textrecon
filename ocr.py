import cv2
import numpy as np
import pytesseract

print("Bun venit la programul pentru extras text din poze.")
img = cv2.imread("ocrsample.png")
img = cv2.resize(img, None, fx=0.5, fy=0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
config = "--psm 3"
text = pytesseract.image_to_string(adaptive_threshold, config=config, lang="eng")
print(text)
cv2.imshow("gray", gray)
cv2.imshow("adaptive th", adaptive_threshold)
print("\nApasa CTRL+Z pentru a iesi din program")
cv2.waitKey(0)