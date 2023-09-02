import time
import threading
import pyautogui
import mouse
import sys
import random as rnd
from pynput.keyboard import Listener, KeyCode
#Import the AFunctions file which is one directory up.
from AFunctions import *

global running
global rounds

ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')

rounds = int (0)
running = False

welcome()


def crabKiller():
    while True:
        if running:
            global rounds
            print ("Let's light em Up! It is round:", rounds)
            if (rounds == 0):
                Compass()
                #Move mouse to the left and down towards middle of screen
                pyautogui.moveRel(rnd.randint(-400, -200), rnd.randint(100, 300), rnd.random() * 0.181 + 0.41)
                upkey()
                Zoomout()
                
            time.sleep(rnd.random() *0.1 + 0.8)
            Notbotting3()
            #move the mouse to the banker between X= 645, 1068, and Y 490, 700
            pyautogui.moveTo(rnd.randint(645, 1068), rnd.randint(490, 700), rnd.random() * 0.181 + 0.41) #Move to banker
            clx()
            Deposit()
            Slot4()
            clx()
            #After grabbing runes, select ores
            Slot3()
            Getitems()
            Xbank()
            if (rounds == 0):
                #"Tap" down the F4 key
                time.sleep(0.03 * rnd.random() + 0.3) 
                pyautogui.keyDown('f4')
                time.sleep(0.03 * rnd.random() + 0.3)
                pyautogui.keyUp('f4')
            
            #move to the spell
            time.sleep(0.03 * rnd.random() + 0.01)
            pyautogui.moveTo(rnd.randint(1695, 1702), rnd.randint(906, 914), rnd.random() * 0.181 + 0.41)
            time.sleep(0.03 * rnd.random() + 0.41)

            #Click on this area 22 times

            for i in range(64):
                clx()
                time.sleep(0.05 * rnd.random() + 0.33)

            if (rounds % rnd.randint(88, 95) == 0 & rounds != 0):
                print ("Let's take a break!")
                Notbotting2()
                time.sleep(0.1 * rnd.random() + rnd.randint(10, 20))

            if (rounds % rnd.randint(9, 12) == 0 & rounds != 0):
                print ("Let's take a short break! We've gained: ", rounds * 16 * 22.5, "EXP" )
                Notbotting2()
                time.sleep(0.1 * rnd.random() + rnd.randint(1, 2))

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