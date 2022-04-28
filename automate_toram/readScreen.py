import pyautogui
import pytesseract
from PIL import Image

# https://pypi.org/project/pytesseract/?msclkid=b9e7a651c5a711ec8909f099e41117af
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def readScreen(a,b, x,y):
    im = pyautogui.screenshot('sample.png', region=(a,b, x,y))
    text = pytesseract.image_to_string(im)
    print(text) 

## Battle logs
#x1 = 29
#x2 = 850
#x3 = 526 -x1
#x4 = 985 -x2 -20
#readScreen(x1, x2, x3, x4)


x1 = 1481
x2 = 221
x3 = 1794 -x1
x4 = 286 -x2
readScreen(x1, x2, x3, x4)


x1 = 1464
x2 = 366
x3 = 1822 -x1
x4 = 436 -x2
readScreen(x1, x2, x3, x4)