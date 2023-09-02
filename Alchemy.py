import time
import sys
import threading
import pyautogui
import mouse
import random as rnd
from pynput.keyboard import Listener, KeyCode
from AFunctions import *


global running
global Clickz
global rnum


ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')

running = False
Clickz = 0
rnum = rnd.randint(80,99)
name = input("What is your name? ")
#welcome()
welcome2(name)

def alcher():
    while True:
        if running:
            global Clickz
            global rnum
            if Clickz == 0:
               print ("Let's RIDE!")

            time.sleep(rnd.random() * 3/27 + 0.43)
            mouse.click() 
            time.sleep(rnd.random() * 3/27 + 0.58)
            Clickz = Clickz + 1

            if (Clickz % rnum == 0):
                time.sleep(rnd.randint(1,3) * rnd.random())
                print ("Time for a break! Rnum value is currently:", rnum)

            if (Clickz % rnd.randint(28,39) == 0):
                time.sleep(rnd.random() * 0.1)

            #After 100 clicks, print the number of clicks
            if ((Clickz % 100 == 0) and (Clickz > 0)):
                print ("You have alched roughly", Clickz * 0.4, "times.")
                rnum = rnd.randint(80,99)
                print ("The new random number is:", rnum)

            if (Clickz == 22400):
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

click_thread = threading.Thread(target=alcher)
click_thread.start()

with Listener(on_press=togglebot) as listner:
    listner.join()

