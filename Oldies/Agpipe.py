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

welcome()

def tubeclick():
    while True:
        if running:
            print("Get ready to crawl!")
            global Tubesent

            if Tubesent == 0:
               print ("Let's get tubular!")
               pyautogui.moveTo(rnd.randint(870,876), rnd.randint(606, 601), rnd.random() * 0.181 + 0.011) #move to center Facing North down

            time.sleep(rnd.random() *2.11 + 0.31)
            mouse.click() #click 
            time.sleep(rnd.random() *2.1 + 0.311)
            mouse.click() #click 

            Tubesent = Tubesent + 1

            if (Tubesent % 17 == 0):
                pyautogui.moveTo(rnd.randint(870,876), rnd.randint(606, 601), rnd.random() * 0.181 + 0.011) #move to center Facing North down


            if (Tubesent % rnd.randint(87,93) == 0):
                print (" We made", Tubesent, "clicks.")
                time.sleep(rnd.randint(1,5) * rnd.random())

            #End of run; time to sleep and repeat     1

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

