import time
import sys
import threading
import pyautogui
import mouse
import random as rnd
from pynput.keyboard import Listener, KeyCode


global running
global dartsMade

ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')

running = False
dartsMade = 0


def winemaker():
    while True:
        if running:
            global dartsMade
            if dartsMade == 0:
               print ("Let's RIDE!")

            time.sleep(rnd.random() * 3/27 + 0.43)
            mouse.click() #click feather
            time.sleep(rnd.random() * 3/27 + 0.58)
            dartsMade = dartsMade + 1

            if (dartsMade % rnd.randint(91,93) == 0):
                time.sleep(rnd.randint(1,3) * rnd.random())
                supsup = True

            if (dartsMade % rnd.randint(28,39) == 0):
                time.sleep(rnd.random() * 0.1)

            if (dartsMade == 201674):
                time.sleep(360) 



        time.sleep(0.0003 * rnd.random() + 0.001)

def togglebot(key):
    if key == ONOFF:
        global running
        print ("Program is on:", not running)
        running = not running
    elif key == KEY: 
        print ("Kill switch acitaved")
        running = False
        exit() # This will end the program entirely
        sys.exit()

click_thread = threading.Thread(target=winemaker)
click_thread.start()

with Listener(on_press=togglebot) as listner:
    listner.join()

