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
burnt = 0
welcome()

#Define a function that calls for a time.sleep if a random number is greater than 0.5

def Timebot():  
    if (rnd.random() > 0.827):
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
            global burnt

            pyautogui.moveTo(rnd.randint(864,950), rnd.randint(375, 480), rnd.random() * 0.081 + 0.18913) #move to top iron ore, follow by a random chance to move within closer bounds
            if (rnd.random() > 0.388):
                pyautogui.moveTo(rnd.randint(912,940), rnd.randint(399, 460), rnd.random() * 0.031 + 0.0218913)
                print("Moving to top ore; 38%", "chance hit")
            time.sleep(rnd.random() *0.31 + 0.531)
            mouse.click() #click 
            time.sleep(rnd.random() *0.28 + 1.811)

            pyautogui.moveTo(rnd.randint(838,996), rnd.randint(816,955), rnd.random() * 0.0832 + 0.181) #move to middle ore, follow by a random chance to move within closer bounds
            if (rnd.random() > 0.381):
                pyautogui.moveTo(rnd.randint(912,940), rnd.randint(851, 912), rnd.random() * 0.031 + 0.0218913)
            time.sleep(rnd.random() *0.31 + 0.531)
            mouse.click() #click 
            time.sleep(rnd.random() *0.26 + 1.811)

            pyautogui.moveTo(rnd.randint(584, 730), rnd.randint(570, 720), rnd.random() * 0.081 + 0.189111) #move to bottom ore, followed by a random chance to move within closer bounds
            if (rnd.random() > 0.381):
                pyautogui.moveTo(rnd.randint(600, 673), rnd.randint(688, 720), rnd.random() * 0.031 + 0.0218913)
            time.sleep(rnd.random() *0.31 + 0.531)
            mouse.click() #click 
            time.sleep(rnd.random() *0.21 + 1.831)


            dug = dug + 3

            if (dug % 24 == 0):
                pyautogui.moveTo(rnd.randint(1670,1886), rnd.randint(600, 765), rnd.random() * 0.181 + 0.011) #move to center Facing North down
                xpus = 1713
                ypus = 765
                for i in range (1, 25):
                    pyautogui.keyDown('shift')
                    pyautogui.moveTo(rnd.randint(xpus - 3, xpus + 3), rnd.randint(ypus - 3, ypus + 3), rnd.random() * 0.093 + 0.107) # move to log 
                    time.sleep(rnd.random() * 0.06 + 0.098)
                    clx() # drop ore
                    burnt = burnt + 1
                    xpus = xpus + 40

                    if ((burnt) % 4 == 0):
                        ypus = ypus + 35 # drop the mouse down one row of items for the next iteration
                        xpus = xpus - 160 # pull mouse back to the first coulum for the next iteration
                        time.sleep( 0.399 + rnd.random() *0.05)
                pyautogui.keyUp('shift')
                Notbotting2()

def togglebot(key):
    if key == ONOFF:
        global running
        print ("Program is on:", not running)
        running = not running
    elif key == KEY: 
        print ("Kill switch acitaved")
        running = False
        sys.exit()

click_thread = threading.Thread(target=tubeclick)
click_thread.start()

with Listener(on_press=togglebot) as listner:
    listner.join()

