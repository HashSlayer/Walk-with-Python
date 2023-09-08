import time
import threading
import pyautogui
import mouse
import sys
import random as rnd
from pynput.keyboard import Listener, KeyCode
#Import the AFunctions file which is one directory up.
from AFunctions import *
from CrabbyFunctions import *

global running
global rounds
global roundset
global falsepot2
global falsepot3
global falsepot4
global falsepot5

ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')

rounds = int (1)
running = False
roundset = int (1)
falsepot2 = False
falsepot3 = False
falsepot4 = False
falsepot5 = False

welcome()


def crabKiller():
    while True:
        if running:
            global rounds
            global roundset
            global falsepot2
            global falsepot3
            global falsepot4
            global falsepot5
            
            print ("Let's light em Up! It is round:", rounds)
            time.sleep(rnd.random() *0.1 + 0.8)
            
            if (rounds == 0):
                Compass()
                pyautogui.moveRel(rnd.randint(-400, -200), rnd.randint(100, 300), rnd.random() * 0.181 + 0.41)
                upkey()
                Zoomout()
                print("Lessss gooo!")
                
            #Reset auto combat by calling jog() and running away and back every 7 rounds
            if (rounds % roundset == 0):
                print ("Let's move!")
                time.sleep(rnd.random() *0.1 + 1.8)
                jog()
                roundset = roundset + 7

            #if statement; every 

            cycle()

            rounds = rounds + 1

def togglebot(key):
    if key == ONOFF:
        global running
        print ("Program is on:", not running)
        running = not running
    elif key == KEY: 
        print ("Kill switch acitaved")
        running = False
        sys.exit() # This will end the program entirely

click_thread = threading.Thread(target=crabKiller)
click_thread.start()

with Listener(on_press=togglebot) as listner:
    listner.join()