#A program that chops two opposing willow trees in Runescape, then drops the logs.

#Imports
import pyautogui
import mouse
import random as rnd
import time
import sys
import threading
from pynput.keyboard import Listener, KeyCode
from AFunctions import *

#Global variables
global running
global rounds
global drops
global roundset

ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')

rounds = int (0)
roundset = int (4)
running = False
drops = int (0)
dropped = int (0)

xpus = 1740
ypus = 770

welcome()

#Define a function "drop" that will drop the logs

def drop():
    #move mouse to the inventory
    pyautogui.moveTo(rnd.randint(1670,1886), rnd.randint(600, 765), rnd.random() * 0.181 + 0.011) #move to center Facing North down
    xpus = 1740
    ypus = 770
    for i in range (1, 2&):
        time.sleep(rnd.random() * 0.1 + 0.1)
        pyautogui.keyDown('shift')
        time.sleep(rnd.random() * 0.1 + 0.1)
        pyautogui.moveTo(rnd.randint(xpus - 3, xpus + 3), rnd.randint(ypus - 3, ypus + 3), rnd.random() * 0.13 + 0.117) # move to log 
        time.sleep(rnd.random() * 0.01 + 0.198)
        mouse.click() # burn log 1 
        dropped = dropped + 1
        xpus = xpus + 40

        if ((dropped) % 4 == 0):
            ypus = ypus + 35 # drop the mouse down one row of items for the next iteration
            xpus = xpus - 160 # pull mouse back to the first coulum for the next iteration
            time.sleep( 0.399 + rnd.random() *0.05)
    pyautogui.keyUp('shift')


#Define Cycles to click on the trees
def cycle():
    #Move the mouse to the first tree at (727, 500)
    pyautogui.moveTo(rnd.randint(727, 770), rnd.randint(468, 500), rnd.random() * 0.1 + 0.41)
    clx()
    time.sleep(rnd.random() * 1 + 14)
    time.sleep(rnd.random())
    #Move the mouse to the second tree at (899, 527) with a 20 pixel varience
    pyautogui.moveTo(rnd.randint(889, 909), rnd.randint(517, 537), rnd.random() * 0.1 + 0.41)
    clx()
    time.sleep(rnd.random() * 1 + 14)
    time.sleep(rnd.random())

def crabKiller():
    while True:
        if running:
            global rounds
            global roundset
            print ("Let's chop em Up! It is round:", rounds)
            time.sleep(rnd.random() *0.1 + 0.8)
            
            if (rounds == 0):
                Compass()
                pyautogui.moveRel(rnd.randint(-400, -200), rnd.randint(100, 300), rnd.random() * 0.181 + 0.41)
                upkey()
                Zoomout()
                print("Lessss gooo!")
                
            #move the mouse to the banker between X= 645, 1068, and Y 490, 700
            if (rounds % roundset == 0):
                print ("Let's get rid of this shit!")
                drop()
                roundset = roundset + rnd.randint(3,4)

            cycle()
            cycle()
            drop()
            time.sleep(rnd.random() *0.1 + 1)
            Notbotting()
            time.sleep(rnd.randint(66, 77) + rnd.random())

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