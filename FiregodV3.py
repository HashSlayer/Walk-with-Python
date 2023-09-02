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
global cycles
global burnt
global logsBurnt

ONOFF = KeyCode(char="`")
KEY = KeyCode(char =' \ ')

welcome()
print ("Let's burn up yo!")
Birdseye()
maxLogs = int(input("Enter the maximum amount of logs availble: "))
print (" Press 1 toggle the bot OFF / ON")
print (" Press ' \ ' to kill the bot, or pull the mouse to the top left corner")
print ("Enjoy the burn!")

cycles = int (0)
burnt = int (0)
logsBurnt = int (0)
xpus = int (1755)
ypus = int(765)
running = False


def burner():
    while True:
        if running:
            print (" ~ T i m e  2  s p a r k  u p ! ~ ")
            global cycles
            global burnt
            global logsBurnt
            global maxLogs

            ## ~~~ Random mouse movement 3 seconds ~~~~ ####
            Notbotting2()
            Birdseye()



            # Begin opening bank: 
            if (cycles % 2 == 0 or cycles == 0):
                print (" Odd session begin.")
                time.sleep(rnd.random() * 0.01 + 0.07) # wait before next action
                pyautogui.moveTo(rnd.randint(1245,1255), rnd.randint(690,730), 0.43 + 0.151 * rnd.random() + 3/27 * rnd.random()) # move mouse to bank, sit at top left of GE.
                time.sleep(rnd.random() * 0.31 + 0.07) # wait before next action
                mouse.click()
                time.sleep(rnd.random() * 0.31 + 0.07) # wait before next action
                pyautogui.moveRel(rnd.randint(-10,10), rnd.randint(-10,14), rnd.random() * 0.43 + 0.9) #Move around from current spot
                Notbotting2()
                print ("Getting wood.")
                Slot2()
                Getall()
                # Moving to burn spot 1
                pyautogui.moveTo(rnd.randint(1504, 1522), rnd.randint(727, 733), rnd.random() * 0.133 + 0.26) # move to burn spot 1 !
                time.sleep(rnd.random() * 0.1 + 0.19)
                pyautogui.moveRel(rnd.randint(-1,1), rnd.randint(1,2), rnd.random() * 0.13 + 0.1) #Move around from current spot
                mouse.click()
                pyautogui.moveRel(rnd.randint(-20,40), rnd.randint(-100,-20), rnd.random() * 0.131 + 0.1) #Move around from current spot
                pyautogui.moveRel(rnd.randint(-32, 42), rnd.randint(6,12), rnd.random() * 0.131 + 0.1) # random movement
                pyautogui.moveRel(rnd.randint(-12, 12), rnd.randint(6,12), rnd.random() * 0.135 + 0.11) # random movement
                time.sleep(rnd.random() * 0.19 + 4.829)

            if (cycles > 0 and (cycles + 1) % 2 == 0): #sesh 2 sesh 2 sesh 2 sesh 2 sesh 2 sesh 2 sesh 2 sesh 2
                print ("Even session begin.")
                pyautogui.moveTo(rnd.randint(1196, 1208), rnd.randint(369,379), 0.43 + 0.5 * rnd.random() + 3/27 * rnd.random()) #move to bank after sesh 1
                time.sleep(rnd.random() * 0.2 + 0.3) # wait before next action, use .1 multiplier because we aren't moving mouse position. 
                mouse.click() # Open up bank
                print("Mouse position at banker to start sesh 2:", pyautogui.position()) # print position
                print ("Getting wood for the even sessions.")
                time.sleep(rnd.random() * .1 + 3.35)                 
                Slot2()
                print (" Let's get ready to burn!!")

                ## pyautogui.moveRel(rnd.randint(0, 5), rnd.randint(38,40), 0.2 + 0.3 * rnd.random()) #Move mouse down to open bank when right clicked
                print("Grabbed wood at at:", pyautogui.position()) # print position  
                pyautogui.moveTo(rnd.randint(1375, 1384), rnd.randint(383, 390), 0.43 + 0.5 * rnd.random() + 3/27 * rnd.random())  #Odd spot beginning   !!!!!!!!!!!!    
                time.sleep((rnd.random() * 0.2 + 0.02)) # Short sleep 
                mouse.click() #Move to spot 2
                pyautogui.moveRel(rnd.randint(-20,40), rnd.randint(-8,12), rnd.random() * 0.131 + 0.1) #Move around from current spot
                pyautogui.moveRel(rnd.randint(-2, 12), rnd.randint(-6,12), rnd.random() * 0.0131 + 0.1) # random movement
                pyautogui.moveRel(rnd.randint(-32, 42), rnd.randint(-6,12), rnd.random() * 0.131 + 0.1) # random movement
                pyautogui.moveRel(rnd.randint(-12, 12), rnd.randint(6,12), rnd.random() * 0.135 + 0.1) # random movement
                time.sleep(4.22 + 0.131 * rnd.random()) # sleep extra for run to spot
                logsBurnt = logsBurnt - 1

            #sesh 2 sesh 2 sesh 2 sesh 2 sesh 2 sesh 2 sesh 2
    
            # BURN PROCESS BEGIN !
            Notbotting3()

            # Time to burn logs, this portion is extensive...
            xpus = 1740
            ypus = 770
            for i in range (1, 23):
                pyautogui.moveTo(rnd.randint(1690,1710), rnd.randint(760, 774), rnd.random() * 0.03 + 0.197) #move to tinder box
                time.sleep(rnd.random() *0.01 + 0.398)
                mouse.click() #use tinder box
                time.sleep(rnd.random() *0.01 + 0.498)
                pyautogui.moveTo(rnd.randint(xpus - 3, xpus + 3), rnd.randint(ypus - 3, ypus + 3), rnd.random() * 0.03 + 0.399) # move to log 
                time.sleep(rnd.random() * 0.01 + 0.488)
                mouse.click() # burn log 1 
                xpus = xpus + 40 # Adjust X Position; moves mouse to right by one item in inventory
                burnt = burnt + 1 #Add to burn count

                if (burnt == 1):
                    time.sleep(rnd.random() *0.09 + 1.51) # Sleep for an extra 0.9 seconds on the first burn
                
                if ((burnt + 1) % 4 == 0 or burnt == 3):
                    ypus = ypus + 35 # drop the mouse down one row of items for the next iteration
                    xpus = xpus - 160 # pull mouse back to the first coulum for the next iteration
                    time.sleep( 0.009 + rnd.random() *0.05)

                if ((burnt + 2) % 4 == 0):
                    time.sleep( 0.01 + rnd.random() *0.001)


            print ("All done!")
            cycles = cycles + 1
            logsBurnt = logsBurnt + 20
            print ("This is batch number:", cycles, "with,", logsBurnt, "logs burnt.")
            print( (maxLogs - logsBurnt), "logs to go.")
            print("Keep it up !")
            time.sleep( 0.01 + rnd.random() *0.001)
            pyautogui.moveTo(rnd.randint(856,864), rnd.randint(560,586), 0.13 + 5/27 * rnd.random()) # move mouse to banker?
            time.sleep( 0.01 + rnd.random() *0.001)
            burnt = 0

            if (logsBurnt > maxLogs):
               print ("Out of logs!")
               sys.exit()

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