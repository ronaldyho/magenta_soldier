import pyautogui, time, pydirectinput 
import random, re
import pytesseract
from PIL import Image

global timeVAL

# https://pypi.org/project/pytesseract/?msclkid=b9e7a651c5a711ec8909f099e41117af
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def getCurrentTime():
    return int(time.time())

def randWait():
    x = random.randint(1,3)
    #print("sleeping")
    #x = 0.5
    time.sleep(x)

def pressF():
    pyautogui.press("f")
    print("press.f")

def press1():
    pyautogui.press("1")
    print("press.1")
    pressF()
    randWait()

def press3():  #evasion
    pyautogui.press("3")
    print("press.3")
    pressF()
    randWait()

def press4():
    pyautogui.press("4")
    print("press.4")
    pressF()
    randWait()

def press7():
    # Warcry of struggle
    pyautogui.press("7")
    print("press.7")
    pressF()
    randWait()

def pressAlt( keyPress ):
    # Healz
    pyautogui.keyDown('alt')  
    pyautogui.press( keyPress )
    time.sleep(3)
    pyautogui.keyUp('alt')  
    print("press.alt." + keyPress)
    pressF()

def checkReviveHere():

    def checkReviveNow():

        a = 1481
        b = 221
        x = 1794 -a
        y = 286 -b

        # Screenshot to local
        im = pyautogui.screenshot('sample.png', region=(a,b, x,y))
        im = pyautogui.screenshot('sample.png', region=(a,b, x,y))
        #im = pyautogui.screenshot(region=(a,b, x,y))
        text = pytesseract.image_to_string(im)

        return re.match("Revive", text)

    def checkReviewHere():
        a = 1464
        b = 366
        x = 1822 -a
        y = 436 -b
        
        # Screenshot to local
        im = pyautogui.screenshot('sample.png', region=(a,b, x,y))
        #im = pyautogui.screenshot(region=(a,b, x,y))
        text = pytesseract.image_to_string(im)

        return re.match("Revive", text)

    boolA = checkReviveNow()

    while boolA:
        print("Revive Now") 
        for x in range(10):
            pyautogui.click(x=1684, y=936) # Struggle button
            time.sleep(1)
        boolA = checkReviveNow()

    boolB = checkReviewHere()

    while boolB:
        print("Revive Here") 
        pyautogui.click(x=1388, y=419) # Revive button
        boolB = checkReviewHere()



def readBattleLogs():
    im = pyautogui.screenshot(region=(29, 842, 526, 998))
    text = tess.image_to_string(im)
    print(text) 

def dragAndPull():
    pyautogui.drag(300, -50, 1, button='right')
    pyautogui.move(-300, 50)
    pressF()

try:
    timeVAL = getCurrentTime()
    
    while True:
        checkReviveHere()
        print(">>>")
    
        for x in range(9):
            time.sleep(1)

            pressF()
            
            if x % 3 == 0:
                press1()

        press7()
        pressF()

        dragAndPull()
        
        
        y = getCurrentTime()
        
        if (y + 60) > timeVAL:
            pressAlt("1")
            print("healz")
            timeVAL = getCurrentTime()
            press3()


########
#        pyautogui.keyDown("alt")
#        pyautogui.keyUp("alt")

#        pydirectinput.press(['left', 'left']) #this is the updated line of code
#        pyautogui.dragTo(100, 200, button='left')     # drag mouse to X of 100, Y of 200 while holding down left mouse button
#        pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
#        pyautogui.drag(30, 0, 2, button='right')   # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button
#        pyautogui.move(200, 50) # move it back


### Sample code - OCR 
#import pytesseract as tess
#from PIL import Image
#img = Image.open('image.png')
#text = tess.image_to_string(img)
#print(text)


except KeyboardInterrupt:
    print('\nDone.')