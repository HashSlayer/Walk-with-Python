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
global Clickz2
global y
global x

ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')

running = False
Clickz = 1
Clickz2 = 1
y =  rnd.randint(69, 420)
x =  8
rnum = rnd.randint(80,99)
welcome()


def alcher():
    while True:
        if running:
            global Clickz
            global rnum
            global Clickz2
            global y
            global x
            if Clickz == 1:
               print ("Let's RIDE!")

            time.sleep(rnd.random() * 0.2 + 0.25)
            clx()
            time.sleep(rnd.random() * 0.1 + 0.2)
            clx()
            if (rnd.random() > 0.99173):
                time.sleep(rnd.random() * 0.1 + 0.01)
                clx()
                time.sleep(rnd.random() * 0.3 + 0.01)
                clx()
                print ("Oops, a triple click!!!")
            time.sleep(rnd.random() * 3/27 + 0.43)
            if (rnd.random() > 0.9789):
                clx()
                print ("Oops, a double click!!")
                if (rnd.random() > 0.96):
                    time.sleep(rnd.random() * 31.17 + 5)
                    print ("Oops asffafw!!!")
            
            if (rnd.random() > 0.999):
                clx()
                qclx()
                qclx()
                qclx()
                if (rnd.random() > 0.5):
                    clx()
                    clx()
            Clickz = Clickz + 1
            Clickz2 = Clickz2 + 1

            #Write a function that sleeps for 6 hours after 3000 clicks

            if (Clickz2 > 210):
                time.sleep(21600)
                print ("Time for a break! A big one!")
                    

            if ((Clickz % rnum == 0)):
                time.sleep(rnd.randint(1,3) * rnd.random())
                print ("Time for a break! Rnum value is currently:", rnum)
                #print the amount of clicks
                print ("The amount of clicks is:", Clickz)
                rnum = rnd.randint(60,420)
                print ("The new random number is:", rnum)



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

