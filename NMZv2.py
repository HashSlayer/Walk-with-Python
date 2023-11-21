# This file is a part of OSWS, a script that iterates through the inventory clicking on potions 4 times then movinng through inventory.
import time
import sys
import threading
import pyautogui
import mouse
import random as rnd
from pynput.keyboard import Listener, KeyCode
from AFunctions import *

global running

global laps
global sips
global pots
global sipped
global rangePotx
global rows

global xpus
global ypus

ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')

running = False
sipped = True
sips = 0
laps = 0
pots = 0
rows = 1
xpus = 1695
rangePotx = 1695
ypus = 765

welcome()
print("Get ready to rumble!!!")


def SipCounter():
    global sips
    global pots
    global xpus
    global rangePotx
    sips = sips
    if (sips >= 4):
        print("Drank 4 sips, moving to next potion next time.")
        xpus = xpus + 40
        sleepy(.01, .1, .1)
        pyautogui.moveTo(rnd.randint(rangePotx - 4, rangePotx + 3), rnd.randint(971, 979), rnd.random() * 0.293 + 0.207) # move to inventory slot # 25 / 28. (RNG potions)
        sleepy(.08, .09, .03)
        print ("Drinking potion at coordinates:", rangePotx, "and 975")
        qclx() # drink one sip of potion
        sleepy(.01, .06, .03)
        pots += 1 
        sips = 0
        if rnd.random() > 0.78:
            Notbotting2()

def PotCounter():
    global pots
    global rows
    global xpus
    global ypus
    global rangePotx
    pots = pots
    if (pots >= 4):
        print("Drank 4 potions, moving to next range potion.")
        ypus += 36 # drop the mouse down one row of items for the next iteration
        xpus -= 160 # pull mouse back to the first coulum for the next iteration
        rangePotx += 40
        time.sleep( 0.0139 + rnd.random() *0.05)
        pots = 0
        rows += 1
        print ("Rows:", rows)
        if (rows >= 7):
            print("Sleeping for ever hours")
            sys.exit()

def Lap():
    global laps
    if (rnd.random() > 0.949388):
        pyautogui.moveTo(rnd.randint(864,930), rnd.randint(395, 480), rnd.random() * 0.081 + 0.28913) 
        clx()
        Notbotting()    
    time.sleep(rnd.random() *1.31 + 12.713)

    if (rnd.random() > 0.98488):
        pyautogui.moveTo(rnd.randint(1039,1196), rnd.randint(886,945), rnd.random() * 0.0832 + 0.281) #move to middle ore, follow by a random chance to move within closer bounds
        clx()
        print("MOOOOOOOOO!")
    time.sleep(rnd.random() *1.681 + 12.713)

    if (rnd.random() > 0.89388):
        pyautogui.moveTo(rnd.randint(584, 730), rnd.randint(570, 660), rnd.random() * 0.081 + 0.289111) 
        clx()
    time.sleep(rnd.random() *1.31 + 11.713)


def NMZ():
    while True:
        if running:
            global sips
            global xpus
            global ypus
            global pots
            global laps
            global rangePotx
            global rows
            global sipped

            Lap()
            laps += 1
            print("Lap:", laps)
            

            if ((rnd.random() > 0.79388)):
                print ("(single sip):", laps / 4, "sip:", sips, "at coordinates:", xpus, "and", ypus, "sipped is:", sipped)
                pyautogui.moveTo(rnd.randint(xpus - 4, xpus + 3), rnd.randint(ypus - 3, ypus + 5), rnd.random() * 0.293 + 0.207) # move to potion
                time.sleep(rnd.random() * 0.36 + 0.1098)
                clx() # drink one sip of potion
                sips += 1
                print ("sips is now:", sips)
                time.sleep(rnd.random() * 0.06 + 0.198)
                SipCounter()
                PotCounter()
            else:
                print("No single sip this lap. Time for one more.")
                Lap()
                laps += 1 
                print("Done with this lap.")
                print("Lap:", laps)

                sleepy(.1, .5)
                pyautogui.moveTo(rnd.randint(xpus - 4, xpus + 3), rnd.randint(ypus - 3, ypus + 5), rnd.random() * 0.293 + 0.207) # move to potion
                sleepy(.1, .25)
                print ("Drinking 2 sips! Potion #:", laps / 4, "sip:", sips, "at:", xpus, "and", ypus)
                clx() # drink one sip of potion
                sips += 1
                print ("sips:", sips)
                sleepy(1.58, .38)
                SipCounter()
                PotCounter()
                pyautogui.moveTo(rnd.randint(xpus - 4, xpus + 3), rnd.randint(ypus - 3, ypus + 5), rnd.random() * 0.193 + 0.107) # move to potion
                sleepy(1.33, .5)
                clx() # second sip
                sips += 1
                print ("sips:", sips)
                sipped = True

            SipCounter()    
            PotCounter()

            if (rows >= 7):
                print("Sleeping for ever hours, FAIL SAFE ACTIVATED.")
                sys.exit()

            print (" Time for another loop!")

def togglebot(key):
    if key == ONOFF:
        global running
        print ("Program is on:", not running)
        running = not running
    elif key == KEY: 
        print ("Kill switch acitaved")
        running = False
        sys.exit()
        time.sleep(900)

click_thread = threading.Thread(target=NMZ)
click_thread.start()

with Listener(on_press=togglebot) as listner:
    listner.join()
