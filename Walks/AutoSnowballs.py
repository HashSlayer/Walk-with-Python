import time
import sys
import os
import threading
import pyautogui
import random as rnd
from pynput.keyboard import Listener, KeyCode
# Get the directory of the current script
current_script_dir = os.path.dirname(__file__)
# Get the parent directory of the current script
parent_dir = os.path.abspath(os.path.join(current_script_dir, '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)
from AFunctions import *
from A2Functions import *
from GUI3 import *


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
y =  rnd.randint(6, 200)
x =  8
rnum = rnd.randint(8,99)
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

            time.sleep(rnd.random() * 3 + 9)
            time.sleep(rnd.random() * 10 + 1.1)
            sleepy(60,30,10)
            if (rnd.random() > 0.61789):
                sleepy(20, 80, 10)
                if (rnd.random() > 0.51789):
                    sleepy(10, 80, 10)

            if (rnd.random() > 0.31789):
                sleepy(20, 70, 20)
            if (rnd.random() > 0.61789):
                sleepy(20, 90, 20)
            if (rnd.random() > 0.81789):
                sleepy(30, 60, 20)
            if (rnd.random() > 0.91789):
                sleepy(30, 60, 20)
            if (rnd.random() > 0.91789):
                sleepy(30, 60, 20)
                if (rnd.random() > 0.91789):
                    sleepy(60, 60, 20)

            if (rnd.random() > 0.8789):
                clx()
                if rnd.random() > 0.6:
                    clx()
                    print ("double click")
            else:  
                qclx()
                if rnd.random() > 0.621:
                    clx()
                    print ("double click")

            if (rnd.random() > 0.9789):
                sleepy(.1, 4, 1)
                clx()
                sleepy(.21, 4, 1)
                clx()
                print ("Oops, a double click!!")

            if (rnd.random() > 0.98173):
                time.sleep(rnd.random() * 0.1 + 0.01)
                clx()
                time.sleep(rnd.random() * 0.01 + 0.01)
                clx()
                print ("Oops, a triple click!!!")
            time.sleep(rnd.random() * 3/27 + 0.43)
            if (rnd.random() > 0.9789):
                sleepy(6, 1, 1)
                clx()
                print ("Oops, a double click!!")
            Clickz = Clickz + 1
            Clickz2 = Clickz2 + 1

            if (Clickz2 % y == 0):
                y = rnd.randint(6, 32)
                print ("The new y value is:", y)
                time.sleep(rnd.random() * 0.1 + rnd.randint(4, x))
                Clickz2 = 0
                if rnd.random() > 0.73:
                    x = x + rnd.randint(1, 3)
                    print ("The new x value is:", x)
                    

            if ((Clickz % rnum == 0)):
                time.sleep(rnd.randint(1,3) * rnd.random())
                if rnd.random() > 0.66:
                    time.sleep(rnd.random() * 0.1 + rnd.randint(1, 5))
                if rnd.random() > 0.4:
                    clx()
                    time.sleep(rnd.random() * (x / 30) + 0.1)
                print ("Time for a break! Rnum value is currently:", rnum)
                rnum = rnd.randint(60,420)
                print ("The new random number is:", rnum)

            #After 100 clicks, print the number of clicks
            if ((Clickz % 10 == 0) and (Clickz > 0)):
                print ("You have", Clickz, "clicks")


            if (Clickz % 8000 == 0):
                #sleep for 12 hours
                #This alchs about 1400 items (4200 clikz)
                print ("Time for a break! A big one!")
                time.sleep(43200)
                sys.exit()



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

#111