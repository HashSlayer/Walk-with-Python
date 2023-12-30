# Adjusted script for screen resolution 1680x1050

import time
import sys
import threading
import pyautogui
import random as rnd
from pynput.keyboard import Listener, KeyCode
from AFunctions import *

# Scaling factors for the new resolution
x_scale = (1440 / 1920)
y_scale = (900 / 1200)

# Adjusted global variables
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
xpus = int(1695 * x_scale)
rangePotx = int(1695 * x_scale)
ypus = int(765 * y_scale)

welcome()
print("Get ready to rumble!!!")

def SipCounter():
    global sips, pots, xpus, rangePotx
    sips = sips
    if (sips >= 4):
        print("Drank 4 sips, moving to next potion next time.")
        xpus = xpus + int(40 * x_scale)
        sleepy(.01, .1, .1)
        pyautogui.moveTo(rnd.randint(int((rangePotx - 4) * x_scale), int((rangePotx + 3) * x_scale)), rnd.randint(int(971 * y_scale), int(979 * y_scale)), rnd.random() * 0.293 + 0.207)
        sleepy(.08, .09, .03)
        print ("Drinking potion at coordinates:", rangePotx, "and 975")
        qclx()
        sleepy(.01, .06, .03)
        pots += 1 
        sips = 0
        if rnd.random() > 0.78:
            Notbotting2()

def PotCounter():
    global pots, rows, xpus, ypus, rangePotx
    pots = pots
    if (pots >= 4):
        print("Drank 4 potions, moving to next range potion.")
        ypus += int(36 * y_scale)
        xpus -= int(160 * x_scale)
        rangePotx += int(40 * x_scale)
        time.sleep(0.0139 + rnd.random() * 0.05)
        pots = 0
        rows += 1
        print ("Rows:", rows)
        if (rows >= 7):
            print("Sleeping for ever hours")
            sys.exit()

def Lap():
    global laps
    if (rnd.random() > 0.949388):
        pyautogui.moveTo(rnd.randint(int(864 * x_scale), int(930 * x_scale)), rnd.randint(int(395 * y_scale), int(480 * y_scale)), rnd.random() * 0.081 + 0.28913)
        clx()
        Notbotting()    
    time.sleep(rnd.random() * 1.31 + 12.713)

    if (rnd.random() > 0.98488):
        pyautogui.moveTo(rnd.randint(int(1039 * x_scale), int(1196 * x_scale)), rnd.randint(int(886 * y_scale), int(945 * y_scale)), rnd.random() * 0.0832 + 0.281)
        clx()
        print("MOOOOOOOOO!")
    time.sleep(rnd.random() * 1.681 + 12.713)

    if (rnd.random() > 0.89388):
        pyautogui.moveTo(rnd.randint(int(584 * x_scale), int(730 * x_scale)), rnd.randint(int(570 * y_scale), int(660 * y_scale)), rnd.random() * 0.081 + 0.289111)
        clx()
    time.sleep(rnd.random() * 1.31 + 11.713)

def NMZ():
    while True:
        if running:
            global sips, xpus, ypus, pots, laps, rangePotx, rows, sipped

            #Lap()
            time.sleep(rnd.random() * 1 + 4)
            laps += 1
            print("Lap:", laps)

            if ((rnd.random() > 0.79388)):
                print ("(single sip):", laps / 4, "sip:", sips, "at coordinates:", xpus, "and", ypus, "sipped is:", sipped)
                pyautogui.moveTo(rnd.randint(int((xpus - 4) * x_scale), int((xpus + 3) * x_scale)), rnd.randint(int((ypus - 3) * y_scale), int((ypus + 5) * y_scale)), rnd.random() * 0.293 + 0.207)
                time.sleep(rnd.random() * 0.36 + 0.1098)
                clx()
                sips += 1
                print ("sips is now:", sips)
                time.sleep(rnd.random() * 0.06 + 0.198)
                SipCounter()
                PotCounter()
            else:
                print("No single sip this lap. Time for one more.")
                #Lap()
                laps += 1 
                print("Done with this lap.")
                print("Lap:", laps)

                sleepy(.1, .5)
                pyautogui.moveTo(rnd.randint(int((xpus - 4) * x_scale), int((xpus + 3) * x_scale)), rnd.randint(int((ypus - 3) * y_scale), int((ypus + 5) * y_scale)), rnd.random() * 0.293 + 0.207)
                sleepy(.1, .25)
                print ("Drinking 2 sips! Potion #:", laps / 4, "sip:", sips, "at:", xpus, "and", ypus)
                clx()
                sips += 1
                print ("sips:", sips)
                sleepy(1.58, .38)
                SipCounter()
                PotCounter()
                pyautogui.moveTo(rnd.randint(int((xpus - 4) * x_scale), int((xpus + 3) * x_scale)), rnd.randint(int((ypus - 3) * y_scale), int((ypus + 5) * y_scale)), rnd.random() * 0.193 + 0.107)
                sleepy(1.33, .5)
                clx()
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
        print ("Kill switch activated")
        running = False
        sys.exit()
        time.sleep(900)

click_thread = threading.Thread(target=NMZ)
click_thread.start()

with Listener(on_press=togglebot) as listener:
    listener.join()
