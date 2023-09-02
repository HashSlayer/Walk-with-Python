import time
import sys
import threading
import pyautogui
import mouse
import random as rnd
from pynput.keyboard import Listener, KeyCode
from AFunctions import *


global running
ONOFF = KeyCode(char="`")
KEY = KeyCode(char ='8')
running = False
Tubesent = 0
dug = 0
xpus = 1715
ypus = 765
burnt = 0

def tubeclick():
    while True:
        if running:
            print("Get ready to crawl!")
            global Tubesent
            global dug
            global xpus
            global ypus
            global burnt

            if Tubesent == 0:
               print ("Let's get tubular!")

            pyautogui.moveTo(rnd.randint(844,950), rnd.randint(375, 480), rnd.random() * 0.181 + 0.313) #move to top iron ore
            time.sleep(rnd.random() *0.11 + 1.531)
            mouse.click() #click 
            time.sleep(rnd.random() *0.1 + 1.811)
            pyautogui.moveTo(rnd.randint(838,996), rnd.randint(816,955), rnd.random() * 0.181 + 0.311) #move to middle ore
            mouse.click() #click 
            time.sleep(rnd.random() *1.1 + 1.811)
            pyautogui.moveTo(rnd.randint(584, 730), rnd.randint(570, 720), rnd.random() * 0.181 + 0.311) #move to bottom ore
            mouse.click() #click 
            time.sleep(rnd.random() *0.1 + 0.01311)
            time.sleep(rnd.random() *1.1 + 1.81311)

            dug = dug + 3
            Tubesent = Tubesent + 1

            if (dug % 24 == 0):
                pyautogui.moveTo(rnd.randint(1670,1886), rnd.randint(600, 765), rnd.random() * 0.181 + 0.011) #move to center Facing North down
                xpus = 1715
                ypus = 765
                for i in range (1, 24):
                    pyautogui.keyDown('shift')
                    pyautogui.moveTo(rnd.randint(xpus - 3, xpus + 3), rnd.randint(ypus - 3, ypus + 3), rnd.random() * 0.13 + 0.117) # move to log 
                    time.sleep(rnd.random() * 0.01 + 0.198)
                    mouse.click() # burn log 1 
                    burnt = burnt + 1
                    xpus = xpus + 40

                    if ((burnt) % 4 == 0):
                        ypus = ypus + 35 # drop the mouse down one row of items for the next iteration
                        xpus = xpus - 160 # pull mouse back to the first coulum for the next iteration
                        time.sleep( 0.399 + rnd.random() *0.05)
                pyautogui.keyUp('shift')

def togglebot(key):
    if key == ONOFF:
        global running
        print ("Program is on:", not running)
        running = not running
    elif key == KEY: 
        print ("Kill switch acitaved")
        running = False
        sys.exit()

click_thread = threading.Thread(target=tubeclick)
click_thread.start()

with Listener(on_press=togglebot) as listner:
    listner.join()

