import time
import sys
import threading
import pyautogui
import mouse
import random as rnd
from pynput.keyboard import Listener, KeyCode
from AFunctions import *


global running
ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')
running = False
dug = 0
xpus = 1715
ypus = 765
zed = 0
welcome()

#Define a function that calls for a time.sleep if a random number is greater than 0.5

def Timebot():  
    if (rnd.random() > 0.947):
        time.sleep(rnd.random() * 0.4 + 0.03)
        if (rnd.random() > 0.917):
            Notbotting()

def tubeclick():
    while True:
        if running:
            print("Get ready to crawl!")
            global dug
            global xpus
            global ypus
            global zed

            if (rnd.random() > 0.0388):
                pyautogui.moveTo(rnd.randint(864,930), rnd.randint(395, 480), rnd.random() * 0.081 + 0.28913) #move to top iron ore, follow by a random chance to move within closer bounds
                if (rnd.random() > 0.388):
                        pyautogui.moveTo(rnd.randint(892,920), rnd.randint(449, 479), rnd.random() * 0.051 + 0.0418913)
                print("Moving to top ore; 38%", "chance hit")
            time.sleep(rnd.random() *0.31 + 0.713)
            qclx()
            if (rnd.random() > 0.976):
                clx()
                print ("Nice double click!") #click
                if (rnd.random() > 0.93):
                    clx()
                    print ("Nice triple click!")
                    if (rnd.random() > 0.93):
                        Notbotting2()
            time.sleep(rnd.random() *0.28 + 0.711)
            Timebot()

            if (rnd.random() > 0.0488):
                pyautogui.moveTo(rnd.randint(939,996), rnd.randint(886,945), rnd.random() * 0.0832 + 0.281) #move to middle ore, follow by a random chance to move within closer bounds
                if (rnd.random() > 0.381):
                    pyautogui.moveTo(rnd.randint(960,990), rnd.randint(891, 942), rnd.random() * 0.051 + 0.0418913)
            time.sleep(rnd.random() *0.281 + 0.713)
            qclx()
            if (rnd.random() > 0.93):
                clx()
                print ("Nice double click!") #click
                if (rnd.random() > 0.93):
                    clx()
                    print ("Nice triple click!")
                    if (rnd.random() > 0.93):
                        Notbotting2()
            Timebot()
            time.sleep(rnd.random() *0.26 + 0.711)

            if (rnd.random() > 0.0388):
                pyautogui.moveTo(rnd.randint(584, 730), rnd.randint(570, 660), rnd.random() * 0.081 + 0.289111) #move to bottom ore, followed by a random chance to move within closer bounds
                if (rnd.random() > 0.381):
                    pyautogui.moveTo(rnd.randint(600, 673), rnd.randint(575, 620), rnd.random() * 0.051 + 0.0418913)
            time.sleep(rnd.random() *0.31 + 0.713)
            qclx()
            if (rnd.random() > 0.939):
                clx()
                print ("Nice double click!") #click
                if (rnd.random() > 0.93):
                    clx()
                    print ("Nice triple click!")
                    if (rnd.random() > 0.93):
                        Notbotting2()
            time.sleep(rnd.random() *0.21 + 0.731)
            Timebot()



            dug = dug + 3

            if (dug % 27 == 0):
                pyautogui.moveTo(rnd.randint(1670,1886), rnd.randint(600, 765), rnd.random() * 0.181 + 0.011) #move to center Facing North down
                xpus = 1713
                ypus = 765
                for i in range (1, 25):
                    pyautogui.keyDown('shift')
                    pyautogui.moveTo(rnd.randint(xpus - 4, xpus + 3), rnd.randint(ypus - 3, ypus + 5), rnd.random() * 0.13 + 0.15) # move to log 
                    time.sleep(rnd.random() * 0.06 + 0.0098)
                    qclx() # drop ore
                    if (rnd.random() > 0.98):
                        clx()
                        print ("Nice double click!")
                    zed = zed + 1
                    xpus = xpus + 40

                    if ((zed) % 4 == 0):
                        ypus = ypus + 35 # drop the mouse down one row of items for the next iteration
                        xpus = xpus - 160 # pull mouse back to the first coulum for the next iteration
                        time.sleep( 0.07139 + rnd.random() *0.15)
                pyautogui.keyUp('shift')

                if (rnd.random() > 0.7848):
                    dug += 3
                    print("Dug:", dug, "times")
                    if rnd.random() > 0.798:
                        Notbotting()

                Notbotting2()

                # sleep for 20 hours if "dug" is equal to or greater than 808 (101 inventories)
                if (dug >= 420):
                    print("Sleeping for ever hours")
                    sys.exit()

def togglebot(key):
    if key == ONOFF:
        global running
        print ("Program is on:", not running)
        running = not running
    elif key == KEY: 
        print ("Kill switch acitaved")
        running = False
        pyautogui.keyUp('shift')
        SystemExit()
        sys.exit()

click_thread = threading.Thread(target=tubeclick)
click_thread.start()

with Listener(on_press=togglebot) as listner:
    listner.join()

