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

            time.sleep(rnd.random() * 3/27 + 0.24)
            clx()
            if (rnd.random() > 0.99173):
                time.sleep(rnd.random() * 0.1 + 0.01)
                clx()
                time.sleep(rnd.random() * 0.01 + 0.01)
                clx()
                print ("Oops, a triple click!!!")
            time.sleep(rnd.random() * 3/27 + 0.43)
            if (rnd.random() > 0.9789):
                clx()
                print ("Oops, a double click!!")
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

            #if statement to right click at a 0.1% chance
            if (rnd.random() > 0.9979):
                time.sleep(rnd.random() * 0.1 + 0.01)
                pyautogui.mouseDown(button='right')
                print (" ~~~~~~~~ Oops, a right click!! ~~~~~~~~~")   

            if (rnd.random() > 0.9996):
                time.sleep(rnd.random() * 0.1 + 0.01)
                #move relative by 1 pixel
                pyautogui.moveRel(rnd.randint(-1, 1), rnd.randint(-1,1), rnd.random() * 0.1 + 0.01) # random movement
                print (" ~~~~~~~~ Oops, we moved!! ~~~~~~~~~")  
                #print mouse position
                print("New position:", pyautogui.position())
                time.sleep(rnd.random() * 0.1 + 0.01)


            if (Clickz % 22400 == 0):
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

