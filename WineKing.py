import time
import threading
import pyautogui
import mouse
import sys
import random as rnd
from pynput.keyboard import Listener, KeyCode

global running
global winecount
global winecount2

ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')

winecount = int (0)
winecount2 = int (0)
running = False
yrt = (0.5 + rnd.random() * 0.1 + 3/27 * rnd.random())


def winemaker():
    while True:
        if running:
            print ("Wine makin time baby!")

            global yrt
            global winecount
            global winecount2

            if (winecount == 0):
                pyautogui.moveTo(rnd.randint(480,1303), rnd.randint(1,13), yrt * 0.9 + 0.18)
                pyautogui.moveRel(rnd.randint(-40, 40), rnd.randint(0,2), yrt * 0.8 + 0.1)
                time.sleep(rnd.random()**2 + 0.1)
            ## ~~~ Random mouse movement ~~~~ ####
            pyautogui.moveTo(rnd.randint(700,980), rnd.randint(100,480), yrt * 0.9 + 0.18)
            pyautogui.moveRel(rnd.randint(-40, 74), rnd.randint(-21,20), yrt * 0.8 + 0.2)
            time.sleep(yrt * 0.812 + 1)
            yrt = (0.32 + rnd.random() + 2/27 * rnd.random())

            #Begin opening bank: 
            pyautogui.moveTo(rnd.randint(880,900), rnd.randint(220,280), yrt) # move mouse to banker.
            yrt = (0.33 + rnd.random()) # change yrt speed
            time.sleep(yrt * 0.1 + 0.01) # wait before next action, use .1 multiplier because we aren't moving mouse position. 
            mouse.click() #open up the bank.
            time.sleep(0.04 + 0.13 * rnd.random()) # sleep.

            pyautogui.moveTo(rnd.randint(1005,1030) ,rnd.randint(820, 831), yrt *0.23 + 0.42) # Move to deposit inventory tab 
            time.sleep(rnd.random() * 13/27 + 0.33) #sleep
            mouse.click() # Deposit all inventory
            time.sleep(rnd.random() * 13/272 + 0.12) #sleep
            print("Position of inv depo click:", pyautogui.position())
            pyautogui.moveRel(rnd.randint(-14, 7), rnd.randint(-11,12), yrt * 0.123 + 0.1) # random movement
            time.sleep(rnd.random() * 0.007) #sleep
            pyautogui.moveTo(rnd.randint(940,950), rnd.randint(132, 149), yrt * 0.2 + 0.23) #move to the grapes 
            time.sleep((rnd.random() * 13/120 + 0.05)) # Sleep
            mouse.right_click() #open grape options
            
            time.sleep((0.12 + rnd.random() * 0.15)) #sleep
            pyautogui.moveRel(rnd.randint(-30,20), rnd.randint(71,73), rnd.random() *0.12 +0.13) #move mouse down to quantity of 14
            time.sleep((rnd.random() * 0.087 + rnd.random() * 0.23 + 0.15))
            mouse.click() # Get the 14 Grapes for the wine
            pyautogui.moveRel(rnd.randint(-12, 12), rnd.randint(-6, 2), yrt * 0.08 + 0.0051) # random movement
            time.sleep(yrt*0.15 + 0.08) #sleep
            print ("Getting water")
            pyautogui.moveTo(rnd.randint(986, 1004), rnd.randint(134, 149), yrt * 0.133 + 0.12) # move to water jug
            yrt = (0.02 + rnd.random() + 33/277 * rnd.random()) # YRT  change
            time.sleep(yrt* 0.0173 + 0.01) #Sleep
            mouse.right_click() #open water jug options now. Last item needed
            time.sleep(0.18 * rnd.random() + 0.2) #sleep
            pyautogui.moveRel(rnd.randint(-30, 27), rnd.randint(101, 114), yrt * 0.12 + 0.23) #move mouse down to quantity of 14
            time.sleep(rnd.random() * 0.19 + 0.19)
            mouse.click() #Get water
            time.sleep( 0.03 + rnd.random() * 0.083 )
            print (" Let's Make Some Wine!")
            #
            # WINE PROCESS BEGIN !
            ## ~~~ Random mouse movement ~~~~ ####
            pyautogui.moveRel(rnd.randint(10,30), rnd.randint(-20,-6), yrt * 0.12 + 0.01) #Move around from current spot
            time.sleep(yrt * 0.03 + 0.01) #Sleep
            yrt = (0.33 + rnd.random() + 2/27 * rnd.random()) # Reset YRT
            ## ~~~ Random mouse movement ~~~~ ####
            pyautogui.moveTo(rnd.randint(1058, 1065), rnd.randint(64, 68), yrt * 0.13 + 0.24) # X of the bank
            time.sleep(0.01 + rnd.random() *0.098)
            mouse.click() #exit bank
            pyautogui.moveRel(rnd.randint(-20, 12), rnd.randint(-6,12), yrt * 0.1 + 0.071) # random movement
            #time.sleep(rnd.random() * 0.0987 + 0.02) #sleep short
            print("Position of bank exit click:", pyautogui.position())

            pyautogui.moveTo(rnd.randint(1758,1762), rnd.randint(865, 872), yrt * 0.21 + 0.25) #use jug of water
            time.sleep(rnd.random() *0.15 + 0.07)
            mouse.click()
            pyautogui.moveTo(rnd.randint(1795, 1800), rnd.randint(865, 872), yrt * 0.23 + 0.05) #use on grapes
            time.sleep(rnd.random() * 0.14 + 0.05)
            mouse.click()
            time.sleep(rnd.random() * 0.1 + 0.03)
            pyautogui.keyDown('space')
            time.sleep(rnd.random() * 0.1 + 0.03)
            pyautogui.keyUp('space')
            time.sleep(rnd.random() * 0.011 + 0.01)

            pyautogui.moveTo(rnd.randint(269, 280), rnd.randint(955, 965), yrt * 0.3 + 0.43) #make wine!
            time.sleep(rnd.random() *0.1 + 0.183)
            mouse.click()
            time.sleep(rnd.random() *0.1 + 0.313)
            pyautogui.moveTo(rnd.randint(300, 877), rnd.randint(305, 788), yrt * 0.38 + 2.0051) # random movement
            time.sleep(rnd.random() *0.1 + 0.013)
            pyautogui.moveRel(rnd.randint(-9, 8), rnd.randint(-8, 8), yrt * 0.38 + 2.0051) # random movement
            winecount = winecount + 1
            winecount2 = winecount2 + 1
            print ("Smells great! This is batch number:", winecount)
            pyautogui.moveTo(rnd.randint(860,940), rnd.randint(190,400), yrt * 0.4 + 0.23) # move mouse to banker.
            if (winecount2 % 76 == 0):
                time.sleep(rnd.randint(30, 100))
                winecount2 == 0
                print ("Break time!")
                print (" We made", winecount, "batches this round.")

            if (winecount2 % 433 == 0):
                time.sleep(rnd.randint(50, 300))
                winecount2 == 0
                print ("Break time!676767")
                print (" We made", winecount, "batches this round.")
            #End of wine run; time to sleep and repeat     
        time.sleep(5.8 + rnd.random() * 0.8) # double this time while making fert.. normally it is 10.8 + x, but for fert is 22

def togglebot(key):
    if key == ONOFF:
        global running
        print ("Program is on:", not running)
        running = not running
    elif key == KEY: 
        print ("Kill switch acitaved")
        running = False
        sys.exit() # This will end the program entirely
        exit()

click_thread = threading.Thread(target=winemaker)
click_thread.start()

with Listener(on_press=togglebot) as listner:
    listner.join()