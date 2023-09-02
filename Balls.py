import time
import threading
import pyautogui
import mouse
import random as rnd
import sys
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
from AFunctions import *

global running
global seshs
global burnt
global balls

ONOFF = KeyCode(char="`")
KEY = KeyCode(char ='8')

welcome()
print ("Enjoy the burn!")

seshs = int (0)
balls = int (0)
running = False



def burner():
    while True:
        if running:
            print (" ~ B a l l s ~ ")
            global seshs
            global balls

            ## ~~~ Random mouse movement ~~~~ ####
            pyautogui.moveTo(rnd.randint(700,980), rnd.randint(100,480), 0.33 + 0.31 * rnd.random() + 3/27 * rnd.random())
            pyautogui.moveRel(rnd.randint(-40, 74), rnd.randint(-1,20), 0.03 + 3/27 * rnd.random())
            time.sleep(0.13 + 3/27 * rnd.random())
            ## ~~~ Random mouse movement ~~~~ ####

            # Move to furnace:
            pyautogui.moveTo(rnd.randint(1290,1308), rnd.randint(400,410), 0.33 + 0.31 * rnd.random() + 3/27 * rnd.random()) #Move mouse to furnace
            time.sleep(rnd.random() * 0.19 + 0.29)
            mouse.click() #Click furnace
            time.sleep(rnd.random() *0.1 + 4.983)
            pyautogui.moveTo(rnd.randint(269, 280), rnd.randint(955, 965), rnd.random() * 0.3 + 0.43) #make balls
            time.sleep(rnd.random() *0.1 + 0.383)
            mouse.click() # Click make balls !
            time.sleep(rnd.random() *0.1 + 0.103)
            pyautogui.keyDown('space')
            time.sleep(rnd.random() + 1)
            pyautogui.keyUp('space')
            time.sleep(rnd.random() * 1.8 + 147)

            # Move to Furnace
            pyautogui.moveTo(rnd.randint(500, 520), rnd.randint(730, 750), rnd.random() * 0.3 + 0.43) #move to bank
            time.sleep(rnd.random() *0.1 + 0.183)
            mouse.click() # move to bank
            pyautogui.moveRel(rnd.randint(-1,1), rnd.randint(1,2), rnd.random() * 0.13 + 0.9) #Move around from current spot
            time.sleep(rnd.random() * 0.21 + 4.43)
            print ("Getting Steel.")
            pyautogui.moveTo(rnd.randint(986, 1004), rnd.randint(206, 212), rnd.random() * 0.133 + 0.46) # move to Steel Bars
            time.sleep(rnd.random()* 0.173 + 0.21) #Sleep
            mouse.right_click() #open Steel Bar options now.
            time.sleep(0.181 * rnd.random() + 0.2) #sleep
            pyautogui.moveRel(rnd.randint(-12, 5), rnd.randint(100, 107), rnd.random() * 0.121 + 0.28) #move mouse down to quantity of ALL
            time.sleep(rnd.random() * 0.19 + 0.29)
            mouse.click() #Get Steel
            time.sleep(rnd.random() * 0.19 + 0.29)

            print ("All done!")
            seshs = seshs + 1
            balls = balls + 27
            print ("This is batch number:", seshs, "with,", (balls * 4) , "balls")
            print( (maxBars - balls), "bars to go.")
            time.sleep( 0.01 + rnd.random() *0.001)
            pyautogui.moveTo(rnd.randint(856,864), rnd.randint(560,586), 0.13 + 5/27 * rnd.random()) # move mouse to banker?

            #End of run; time to sleep and repeat     
        time.sleep(rnd.random() * rnd.random() + 0.03)


def togglebot(key):
    if key == ONOFF:
        global running
        print ("Program is on:", not running)
        running = not running
    elif key == KEY: 
        print ("Kill switch acitaved")
        running = False
        sys.exit()

click_thread = threading.Thread(target=burner)
click_thread.start()

with Listener(on_press=togglebot) as listner:
    listner.join()