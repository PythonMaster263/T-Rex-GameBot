import pyautogui
import time
from PIL import Image, ImageGrab
#from numpy import asarray



#def draw():
def isCollide(data):
    for i in range(180, 260):
        for j in range(400, 467):
            if data[i, j] < 100:
                pyautogui.press('up')
                return True

    for i in range(180, 260):
        for j in range(200, 400):
            if data[i, j] < 100:
                pyautogui.press('down')
                return True
    return False



if __name__ == '__main__':
    print('T-Rex Game is about to Start in 3 seconds')
    time.sleep(3)
    pyautogui.press('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
