import time
import sys
import threading
import pyautogui
import mouse
import random as rnd
from pynput.keyboard import Listener, KeyCode
from AFunctions import *


global running
global dartsessions

ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')

dartsessions = int (0)
supsup = False
running = False
maxDarts = int(input("Enter the maximum amount of darts availble: "))
maxClix = int (maxDarts / 10)

print ( "You are set to execute," + str(maxClix) , " clicks. Press 1 to start & stop the program; press 2 to exit completely.")
dartsMade = 0


def winemaker():
    while True:
        if running:
            global dartsessions
            global supsup
            global maxClix
            global dartsMade
            if dartsessions == 0:
               print ("Bronco nation, Let's RIDE!")
            pyautogui.moveTo(rnd.randint(1762,1765), rnd.randint(866, 877), rnd.random() * 0.00181 + 0.011) #move to feather
            time.sleep(rnd.random() *0.0011 + 0.001)
            mouse.click() #click feather
            time.sleep(rnd.random() *0.001 + 0.0011)

            if (dartsessions % rnd.randint(87,90) == 0):
                print (" We made", dartsessions * 10, "darts this round.")
                time.sleep(rnd.randint(1,3) * rnd.random())
                supsup = True
            #End of wine run; time to sleep and repeat     
            pyautogui.moveTo(rnd.randint(1795, 1800), rnd.randint(860, 870), rnd.random() * 0.018 + 0.01) #move to dart tip
            time.sleep(rnd.random() * 0.00184 + 0.0011)
            mouse.click() #click dart tip
            time.sleep(rnd.random() *0.0061 + 0.00171)

            if (dartsessions % rnd.randint(28,39) == 0):
                print (" It is session:", dartsessions, ".")
                time.sleep(rnd.random() * 2)
                supsup = True
            
            dartsessions = dartsessions + 1
            dartsMade = dartsessions * 10

            if (dartsessions >= maxClix):
                print("Max clix reached.")
                sys.exit("Max clicks reached")

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

