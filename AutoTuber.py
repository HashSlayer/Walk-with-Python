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
global item1
global item2
global SleepWeight

ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')

running = False
Clickz = 1
Clickz2 = 1
SleepWeight = .7


item1 = 20000 #Amount of item 1
item2 = 6 #Amount of item 2
1

y =  rnd.randint(69, 420)
x =  8
rnum = rnd.randint(80,99)
welcome()

#Define a function that moves the mouse 40 pixels to the right; holds mouse click down, moves back to the left 40 pixels, and releases the mouse click, with a variance of 2 pixels
def MoveIt():
    #moves the mouse 40 pixels to the right; holds mouse click down, moves back to the left 40 pixels, and releases the mouse click, with a variance of 2 pixels
    pyautogui.moveRel(rnd.randint(38, 42), rnd.randint(-2, 2), rnd.random() * 0.1 + 0.3)
    pyautogui.mouseDown(button='left')
    pyautogui.moveRel(rnd.randint(-42, -38), rnd.randint(-2, 2), rnd.random() * 0.1 + 0.3)
    sleepy(.5, .2)
    pyautogui.mouseUp(button='left')
    sleepy(2, 1)
    #Press down the f4 key
    pyautogui.keyDown('f4')
    sleepy(.1, .1)
    #Release the f4 key
    pyautogui.keyUp('f4')
    sleepy(1, 1)


def alcher():
    while True:
        if running:
            global Clickz
            global rnum
            global Clickz2
            global y
            global x
            global item1
            global item2
            global SleepWeight

            if Clickz == 1:
               print ("Let's RIDE!")
               item1 *= 2.9
               item2 *= 2.9

            sleepy(1.3, (SleepWeight / 2), 0.1)
            if (rnd.random() > 0.12069):
                sleepy(1.2, (SleepWeight / 2), 0.11)
            if (rnd.random() > 0.0943):
                qclx()
            else:
                clx()
            
            if (rnd.random() > 0.989903):
                SleepWeight += .005
                sleepy(.05, SleepWeight)
                print ("SleepWeight is now:", SleepWeight) 
                if (rnd.random() > 0.6903):
                    sleepy(.1, SleepWeight)
                    if (rnd.random() > 0.8903):
                        clx()
                    if (rnd.random() > 0.8903):
                        sleepy(.1, SleepWeight)

            if (rnd.random() > 0.98173):
                time.sleep(rnd.random() * 0.1 + 0.011)
                qclx()
                time.sleep(rnd.random() * 0.1 + 0.01)
                qclx()
                print ("Oops, a triple click!!!")
            time.sleep(rnd.random() * 3/27 + 0.43)

            if (rnd.random() > 0.9889):
                clx()
                print ("Oops, a double click!!")
                for i in range(0, rnd.randint(1, 32)):
                    time.sleep(rnd.random() * 0.001 + 0.001)
                    if (rnd.random() > 0.9):
                        qclx()
                        if (rnd.random() > 0.69):
                            clx()
                            print ("Ultra Bang!!")

            if (rnd.random() > 0.7889):
                sleepy(.1, 1)
                if (rnd.random() > 0.58):
                    sleepy(.1, 1)
                    if (rnd.random() > 0.67):
                        for i in range(0, rnd.randint(1, 7)):
                            sleepy(.01, 0.09)
                            qclx()


    

            if ((rnd.random() > 0.9889) and (Clickz > rnd.randint(1000, 2000))):
                sleepy(1, rnd.randint(7, 9))
                print ("Oops, a big sleepy!!")
                if (rnd.random() > 0.7):
                    sleepy(1, 9)
                    if (rnd.random() > 0.9):
                        for i in range(0, rnd.randint(1, 5)):
                            sleepy(.01, 1)
 

            if ((rnd.random() > 0.9989) and (Clickz > rnd.randint(2000, 4200))):
                sleepy(10, 320)
                print ("Oops, a big sleepy!!")

            Clickz = Clickz + 1
            Clickz2 = Clickz2 + 1

            if (Clickz2 % y == 0):
                y = rnd.randint(69, 420)
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
            if ((Clickz % 100 == 0) and (Clickz > 0)):
                print ("You have", Clickz, "clicks")

            if (Clickz % item1 == 0):
                sys.exit()
                MoveIt()


            if (Clickz % (item1) == 0):
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

