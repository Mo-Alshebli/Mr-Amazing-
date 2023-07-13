import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread("e.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)
print(text)