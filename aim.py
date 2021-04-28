from PIL import Image, ImageGrab
import pyautogui
from time import sleep
import mouse
sleep(5)
import time
tty = True
walk = True
while tty:
    img = ImageGrab.grab( (422, 1306, 423, 1307) )
    img.save("D:/HTML/aim/screens/food.png", "BMP")
    img = ImageGrab.grab( (319, 1307, 320, 1308) )
    img.save("D:/HTML/aim/screens/water.png", "BMP")
    img = ImageGrab.grab( (281, 1385, 282, 1386) )
    img.save("D:/HTML/aim/screens/health.png", "BMP")
    # img = ImageGrab.grab( (888, 652, 889, 653) )
    # img.save("D:/HTML/aim/screens/waterIcon.png", "BMP")i
    # mouse.move(100, 100, absolute=False, duration=2)
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.1
    #colorF = list(img.getdata())
    #print("\ncolorFood", colorF)
    #iprint(pyautogui.position())

    # #walk1
    # pyautogui.keyDown("w")
    # sleep(1)
    # pyautogui.keyUp("w")
    # sleep(0.2)
    # pyautogui.keyDown("s")
    # sleep(1)
    # pyautogui.keyUp("s")

    # food
    # col = Image.open('D:/HTML/aim/screens/food.png', 'r')
    # colorF = list(col.getdata())
    # print("\ncolorFood", colorF)

    # if colorF != [(249, 249, 249)]:
    #     walk = False
    #     pyautogui.press("Esc")
    #     print("FOOD IS RED")
    #     tty = False
    #     break
    # else:
    #     print("FOOD IS OK")

    #walk2
    # pyautogui.keyDown("w")
    # sleep(1)
    # pyautogui.keyUp("w")
    # sleep(0.2)
    # pyautogui.keyDown("s")
    # sleep(1)
    # pyautogui.keyUp("s")

    #water
    # col = Image.open('D:/HTML/aim/screens/water.png', 'r')
    # colorW = list(col.getdata())
    # if colorW != [(246, 246, 246)]:
    #     pyautogui.press('i')
    #     pyautogui.moveTo(286, 858)
    #     sleep(0.5)
    #     pyautogui.click()
    #     water = pyautogui.locateCenterOnScreen('D:/HTML/aim/screens/waterIcon.png')
    #     pyautogui.moveTo(water)
    #     pyautogui.click(clicks=2, interval=0.1)
    #     sleep(5)
    #     pyautogui.press('esc')
    #     sleep(4)
    # if colorW == [(246, 246, 246)]:
    #     print("WATER IS OK NOW")
    #     sleep(2)
    #     #tty = False
        
    # else:
    #     print("WATER IS OK")

    #walk3
    # pyautogui.keyDown("w")
    # sleep(1)
    # pyautogui.keyUp("w")
    # sleep(0.2)
    # pyautogui.keyDown("s")
    # sleep(1)
    # pyautogui.keyUp("s")

    #health
    col = Image.open('D:/HTML/aim/screens/health.png', 'r')
    colorH = list(col.getdata())
    #print(colorH)

    if colorH != [(250, 250, 250)]:
        #print("STOP\n")
        pyautogui.press("Esc")
        print("LOW HEALTH")
        #break
        tty = False
    else:
        print("HEALTH IS OK")
