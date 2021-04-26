from PIL import Image, ImageGrab
import pyautogui
from time import sleep
colorWI = [(77, 104, 99)]
sleep(5)
import time
tty = True
while tty:
    img = ImageGrab.grab( (422, 1306, 423, 1307) )
    img.save("food.png", "BMP")
    img = ImageGrab.grab( (319, 1307, 320, 1308) )
    img.save("water.png", "BMP")
    img = ImageGrab.grab( (269, 1382, 270, 1383) )
    img.save("health.png", "BMP")
    # img = ImageGrab.grab( (888, 652, 889, 653) )
    # img.save("waterIcon.png", "BMP")
    #colorWI = list(img.getdata())
    #print(colorWI)
    #(888, 652, 889, 653,0x4d6863)

#

    pyautogui.FAILSAFE = True
    #colorF = list(img.getdata())
    #print("\ncolorFood", colorF)
    #print(pyautogui.position())

    #walk
    # def hold_key(key, hold_time):
    #     start = time.time()
    #     while time.time() - start < hold_time:
    #         pyautogui.keyDown(key)
    #         hold_key('w', 2)
    #         hold_key('s', 2)
    #         tty = False

    # food
    col = Image.open('food.png', 'r')
    colorF = list(col.getdata())
    #print("\ncolorFood", colorF)

    if colorF != [(249, 249, 249)]:
        #print("STOP\n")
        pyautogui.press("Esc")
        print("FOOD IS RED")
        #break
        tty = False
    else:
        print("FOOD IS OK")

    #water
    col = Image.open('water.png', 'r')
    colorW = list(col.getdata())
    if colorW == [(246, 246, 246)]:
        pyautogui.press('i')
        # pyautogui.moveTo(885, 604, 1)
        water = pyautogui.locateCenterOnScreen('waterIcon.png')
        print(water)
        pyautogui.moveTo(water)
        pyautogui.click(clicks=2, interval=0.1)
        sleep(5)
        pyautogui.press('esc')
        sleep(2)
    if colorW == [(246, 246, 246)]:
        print("WATER IS OK NOW")
        sleep(2)
        tty = False
        
    else:
        print("WATER IS OK")

    #health
    # col = Image.open('health.png', 'r')
    # colorH = list(col.getdata())
    # print(colorH)

    # if colorH != [(206, 206, 203)]:
    #     #print("STOP\n")
    #     pyautogui.press("Esc")
    #     print("LOW HEALTH")
    #     #break
    #     tty = False
    # else:
    #     print("HEALTH IS OK")