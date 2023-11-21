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
global xpus
global ypus
global pots
global rangePotx
global rows
global didsip

ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')
running = False
didsip = True
sips = 0
laps = 0
pots = 0
rows = 1

xpus = 1695
rangePotx = 1695
ypus = 765

welcome()
print("Get ready to scream.!")

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
            global didsip

            if (rnd.random() > 0.949388):
                pyautogui.moveTo(rnd.randint(864,930), rnd.randint(395, 480), rnd.random() * 0.081 + 0.28913) 
                qclx()
            Notbotting()    
            time.sleep(rnd.random() *1.31 + 12.713)

            if (rnd.random() > 0.98488):
                pyautogui.moveTo(rnd.randint(1039,1196), rnd.randint(886,945), rnd.random() * 0.0832 + 0.281) #move to middle ore, follow by a random chance to move within closer bounds
                qclx()
                print("MOOOOOOOOO!")
            time.sleep(rnd.random() *1.681 + 12.713)

            if (rnd.random() > 0.89388):
                pyautogui.moveTo(rnd.randint(584, 730), rnd.randint(570, 660), rnd.random() * 0.081 + 0.289111) 
                qclx()
            time.sleep(rnd.random() *1.31 + 11.713)
            laps += 1
            print("Lap:", laps)

            if (didsip == False and sips < 3):
                pyautogui.moveTo(rnd.randint(xpus - 4, xpus + 3), rnd.randint(ypus - 3, ypus + 5), rnd.random() * 0.293 + 0.207) # move to inventory slot
                time.sleep(rnd.random() * 0.26 + 0.1098)
                qclx() # drink one sip of potion
                print ("On Drink (double sipping):", laps / 4, "sip:", sips + 1, "at coordinates:", xpus, "and", ypus)
                time.sleep(rnd.random() * 0.76 + 1.698)
                clx() # second sip
                sips += 2
                didsip = True
                didsip = True


            if ((rnd.random() > 0.72388 or sips >= 3) and didsip == True):
                pyautogui.moveTo(rnd.randint(xpus - 4, xpus + 3), rnd.randint(ypus - 3, ypus + 5), rnd.random() * 0.293 + 0.207) # move to inventory slot
                time.sleep(rnd.random() * 0.36 + 0.1098)
                qclx() # drink one sip of potion
                sips += 1
                print ("On Drink:", laps / 4, "sip:", sips + 1, "at coordinates:", xpus, "and", ypus)
                time.sleep(rnd.random() * 0.06 + 0.098)
                if rnd.random() > 0.88:
                    Notbotting2()
            else:
                print("No singular potion drink this lap.")
                time.sleep(rnd.random() * 0.06 + 0.88)
                didsip = False
                if rnd.random() > 0.88:
                    Notbotting2()    

 #           pyautogui.moveTo(rnd.randint(xpus - 4, xpus + 3), rnd.randint(ypus - 3, ypus + 5), rnd.random() * 0.293 + 0.207) # move to inventory slot
  #          time.sleep(rnd.random() * 0.36 + 0.1098)
   #         qclx() # drink one sip of potion
    #        print ("On Drink:", laps / 4, "sip:", sips + 1, "at coordinates:", xpus, "and", ypus)
     #       time.sleep(rnd.random() * 0.06 + 0.098)
      #      if rnd.random() > 0.88:
       #         Notbotting2()

 
            if (sips >= 4):
                print("Drank 4 sips, moving to next potion next time.")
                xpus = xpus + 40
                time.sleep( 0.1 + rnd.random() *0.1)
                pyautogui.moveTo(rnd.randint(rangePotx - 4, rangePotx + 3), rnd.randint(971, 979), rnd.random() * 0.293 + 0.207) # move to inventory slot # 25 / 28. (RNG potions)
                time.sleep(rnd.random() * 0.09 + 0.18)
                print ("Drinking potion at coordinates:", rangePotx, "and 975")
                clx() # drink one sip of potion
                time.sleep(rnd.random() * 0.06 + 0.098)
                pots = pots + 1 
                Notbotting3()
                if rnd.random() > 0.78:
                    Notbotting2()
                sips = 0

            if (pots >= 4):
                print("Drank 4 potions, moving to next range potion.")
                ypus = ypus + 36 # drop the mouse down one row of items for the next iteration
                xpus = xpus - 160 # pull mouse back to the first coulum for the next iteration
                rangePotx = rangePotx + 40
                time.sleep( 0.1139 + rnd.random() *0.15)
                pots = 0
                rows += 1
                print ("Rows:", rows)
                if (rows >= 7):
                    print("Sleeping for ever hours")
                    sys.exit()

            if (rows >= 7):
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

click_thread = threading.Thread(target=NMZ)
click_thread.start()

with Listener(on_press=togglebot) as listner:
    listner.join()
