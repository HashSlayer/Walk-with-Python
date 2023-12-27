import time
import sys
import threading
import pyautogui
import random as rnd
from pynput.keyboard import Listener, KeyCode
from AFunctions import *


global running
global Clickz
global rnum
global Clickz2
global y
global x
global items

ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')

running = False
Clickz = 1

items = 2743 #Amount of item 1

y =  rnd.randint(69, 420)
x =  8
rnum = rnd.randint(80,99)
welcome()


def ransleep():
    if (rnd.random() > 0.9803):
        sleepy(.05, .1, .1)
        if (rnd.random() > 0.6903):
            sleepy(.1)

    if (rnd.random() > 0.7889):
        sleepy(.1, 1)
        if (rnd.random() > 0.58):
            sleepy(.1, 1)
            
    if ((rnd.random() > 0.9889) and (Clickz > rnd.randint(1000, 2000))):
        sleepy(1, rnd.randint(7, 9))
        print ("Oops, a big sleepy!!")
        if (rnd.random() > 0.7):
            sleepy(1, 9)

 

            if ((rnd.random() > 0.9989) and (Clickz > rnd.randint(2000, 4200))):
                sleepy(10, 320)
                print ("Oops, a big sleepy!!")




def alcher():
    while True:
        if running:
            global Clickz
            global rnum
            global y
            global x
            global items

            if Clickz == 1:
               print ("Let's Click!")
               print ("Clicking initiated at time:", time.strftime("%H:%M:%S", time.localtime())) 

            sleepy(1.9, .25, .09)
            if (rnd.random() > 0.22743):
                sleepy(.1, .1, .1)
            if (rnd.random() > 0.00343):
                clx()
            else:
                print ("No click")
            
            ransleep()

            sleepy(1.9, .25, .09)
            if (rnd.random() > 0.3743):
                sleepy(.1, .1, .1)
            if (rnd.random() > 0.0343):
                if (rnd.random() > 0.051):
                    clx()
            else:
                qclx()
            
            ransleep()

            if (rnd.random() > 0.9789):
                clx()
                print ("Oops, a double click!!")
                for i in range(0, rnd.randint(1, 32)):
                    time.sleep(rnd.random() * 0.01 + 0.01)
                    if (rnd.random() > 0.78):
                        qclx()
                        print ("Ultra Bang!!")

            if (rnd.random() > 0.9789):
                clx()
                print ("Oops, a double click!!")
                if (rnd.random() > 0.96):
                    sleepy(3,30)
                    print ("Oops asffafw!!!")

            if (rnd.random() > 0.9489):
                sleepy(0.1, 5, .1)
                print ("5 precent chance sleep")

            Clickz = Clickz + 1

            #After 100 clicks, print the number of clicks
            if ((Clickz % 100 == 0) and (Clickz > 0)):
                print ("You have", Clickz, "clicks")

            if (Clickz % items == 0):
                sys.exit()

            if (Clickz % (items) == 0):
                sleepy(6, 1, 1)
                clx()
                if rnd.random() > 0.4:
                    sleepy(1, 1)
                    clx()
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

