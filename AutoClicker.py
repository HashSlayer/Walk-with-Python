import time
import sys
import threading
import pyautogui
import random as rnd
from pynput.keyboard import Listener, KeyCode
from AFunctions import *


global running
global clickCount
global x
global y

ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')

running = False
clickCount = 1

y =  rnd.randint(69, 420)
x =  input("How many seconds would you like between each click?")
randomNumber = rnd.randint(80,99)
welcome()

#This auto clicker will have a variance of 1/11; Example, if you set the clicks at an interval of 1 minute
#It will click every 60 +/- 6.6 seconds. 

def alcher():
    while True:
        if running:
            global clickCount
            global randomNumber
            global y
            global x
            if clickCount == 1:
               print ("Let's RIDE!")
            
            #THE HEART OF THE PROGRAM :)
            sleepy(x, x/11, x/30)
            clx()
            #THE HEART OF THE PROGRAM :)

            if (rnd.random() > 0.98173):
                time.sleep(rnd.random() * (x / 100))
                clx()
                sleepy()
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
            clickCount = clickCount + 1
            clickCount2 = clickCount2 + 1

            #Write a function that sleeps for 6 hours after 3000 clicks

            if (clickCount2 > 210):
                time.sleep(21600)
                print ("Time for a break! A big one!")
                    

            if ((clickCount % randomNumber == 0)):
                time.sleep(rnd.randint(1,3) * rnd.random())
                print ("Time for a break! randomNumber value is currently:", randomNumber)
                #print the amount of clicks
                print ("The amount of clicks is:", clickCount)
                randomNumber = rnd.randint(60,420)
                print ("The new random number is:", randomNumber)



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

