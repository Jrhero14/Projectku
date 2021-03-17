from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    RestartBtn = (342,389)
    Dinosaur = (169,392)

def RestartGame():
    pyautogui.click(Cordinates.RestartBtn)

def DinoLompat():
    pyautogui.press('space')

def Trigger(x1, y1, x2, y2):
    box = (x1, y1, x2, y2)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors()) 
    #print(int(a.sum()))
    return (int(a.sum()))

def EmergencyTrigger1(x1e1, y1e1, x2e1, y2e1):
    box = (x1e1, y1e1, x2e1, y2e1)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    #print(int(a.sum()))
    return (int(a.sum()))

def EmergencyTrigger2(x1e2, y1e2, x2e2, y2e2):
    box = (x1e2, y1e2, x2e2, y2e2)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    #print(int(a.sum()))
    return (int(a.sum()))

def EmergencyTrigger3(x1e3, y1e3, x2e3, y2e3):
    box = (x1e3, y1e3, x2e3, y2e3)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    #print(int(a.sum()))
    return (int(a.sum()))

# 1 - 11 GrayValue = 1146
# 2 - 21
# 3 - 31
# Fast - 41 GracyValue = 5486

x1, y1, x2, y2 = 258, 389, 267, 420 # Trigger Biasa

TimeBegin = time.time()
TriggerValue = 526
RestartGame()

while True:
    # if (Trigger(256, 385, 385, 422) != 5020):
    #     pyautogui.click(798,351)
    #     break
    # EmergencyTrigger2(195, 386, 274, 420)
    TimeEnd = time.time()
    if (Trigger(x1, y1, x2, y2) != TriggerValue):
        DinoLompat()
        print("JumpNormal", Trigger(x1, y1, x2, y2), x2)
    elif(Trigger(222, 389, 231, 420) != 526):
        DinoLompat()
        print("JumpEmergency1")
    elif(Trigger(208, 389, 217, 420) != 526):
        DinoLompat()
        print("JumpEmergency2")
    elif (Trigger(248, 389, 257, 420) != 526):
        DinoLompat()
        print("JumpEmergency3")

    if ((TimeEnd-TimeBegin) > 100):
        x1, y1, x2, y2 = 318, 389, 327, 420
        if (Trigger(256, 385, 385, 422) != 5020):
            DinoLompat()
            print("All3")
    if ((TimeEnd-TimeBegin) > 90):
        x1, y1, x2, y2 = 298, 389, 307, 420
        if (Trigger(235, 386, 314, 420) != 2933):
            DinoLompat()
            print("All2")
    if ((TimeEnd-TimeBegin) > 41):
        x1, y1, x2, y2 = 278, 389, 287, 420
        if (Trigger(235, 386, 314, 420) != 2933):
            DinoLompat()
            print("All")



