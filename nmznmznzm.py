import time
import sys
import os
import threading
import random as rnd
from pynput.keyboard import Listener, KeyCode, Key
# Get the directory of the current script
current_script_dir = os.path.dirname(__file__)
# Get the parent directory of the current script
parent_dir = os.path.abspath(os.path.join(current_script_dir, '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)
from Utilities.MainFunctions import *
from Utilities.Movement import *
import tkinter as tk
from tkinter import font as tkFont
from datetime import datetime
from Utilities.Conffeti import *
from Utilities.Banking import *


# Scaling factors for the new resolution

# Adjusted global variables
global running, sips, pots, sipped

ONOFF = Key.alt_l  # Left Alt key for toggling on/off
KEY = Key.alt_r  # Right Alt key to exit the program

running_lock = threading.Lock()
bot_thread = None

running = False
sipped = True
sips = 0
pots = 0
rows = 1
pot_number = 0
skill_pot_number = 25 #25-28


welcome()
print("Get ready to Rumble!")

def SipCounter():
    global sips, pots
    sips = sips
    if (sips >= 4):
        print("Drank 4 sips, moving to next potion next time.")
        pots += 1
        sleep(.1)
        inv_slot(skill_pot_number)
        sleep(.08, .09, .03)
        pots += 1 
        sips = 0

def PotCounter():
    global pots, rows
    pots = pots
    if (pots >= 4):
        print("Drank 4 potions, moving to next range potion.")
        sleep(.05, .1)
        pots = 0
        rows += 1
        print ("Rows:", rows)
        if (rows >= 7):
            print("Sleeping for ever hours")
            sys.exit()


def NMZ():
    while True:
        if running:
            global sips, pots, rows, sipped

            sleep(10, 3)
            if rnd.random() > 0.889:
                Notbotting()
                Notbotting()
            sleep(10, 3)
            if rnd.random() > 0.289:
                    Notbotting()

            print("Starting loop!")

            if ((rnd.random() > 0.79388)):
                inv_slot(pots)
                sips += 1
                print ("sips is now:", sips)
                time.sleep(rnd.random() * 0.06 + 0.198)
                SipCounter()
                PotCounter()
            else:
                print("No single sip this lap. Time for one more.")
                sleep(6, 3, 2)
                if rnd.random() > 0.889:
                    Notbotting()
                    Notbotting()
                sleep(14, 3, 2)
                if rnd.random() > 0.289:
                    Notbotting()
                    if rnd.random() > 0.889:
                        Notbotting2()
                print("Starting loop!")
                sleep(.1, .5)
                inv_slot(pots)
                sleep(.3, .3, .25)
                sips += 1
                print ("sips:", sips)
                sleep(1.6, .4)
                SipCounter()
                PotCounter()
                inv_slot(pots)
                sips += 1
                print ("sips:", sips)
                sipped = True
            SipCounter()    
            PotCounter()
            if (rows >= 7):
                print("Sleeping for ever hours, FAIL SAFE ACTIVATED.")
                sys.exit()
            print (" Time for another loop!")
        #Not Running
    #Not True
#End of NMZ()

def togglebot(key):
    if key == ONOFF:
        global running
        print ("Program is on:", not running)
        running = not running
    elif key == KEY: 
        print ("Kill switch activated")
        running = False
        sys.exit()

click_thread = threading.Thread(target=NMZ)
click_thread.start()

with Listener(on_press=togglebot) as listener:
    listener.join()
