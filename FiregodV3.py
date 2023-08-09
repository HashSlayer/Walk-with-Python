import time
import threading
import pyautogui
import mouse
import random as rnd
import sys
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

global running
global seshs
global burnt
global logsBurnt

ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='`')

print ("Let's burn up yo!")
print ("Dont forget to face North at bird's eye, 5 notches zoomed in! 7 West and 3 North of the NE GE corner")
maxLogs = int(input("Enter the maximum amount of logs availble: "))
print (" Press 1 toggle the bot OFF / ON")
print (" Press '`' to kill the bot, or pull the mouse to the top left corner")
print ("Enjoy the burn!")

seshs = int (0)
burnt = int (0)
logsBurnt = int (0)
xpus = int (1755)
ypus = int(765)
running = False


def burner():
    while True:
        if running:
            print (" ~ T i m e  2  s p a r k  u p ! ~ ")
            global seshs
            global burnt
            global logsBurnt
            global maxLogs

            ## ~~~ Random mouse movement ~~~~ ####
            pyautogui.moveTo(rnd.randint(700,980), rnd.randint(100,480), 0.33 + 0.31 * rnd.random() + 3/27 * rnd.random())
            pyautogui.moveRel(rnd.randint(-40, 74), rnd.randint(-1,20), 0.03 + 0.31 * rnd.random() + 3/27 * rnd.random())
            time.sleep(0.13 + 3/27 * rnd.random())
            ## ~~~ Random mouse movement ~~~~ ####

            # Must be true north at 5 mouse notches zoomed in

            # Begin opening bank: 
            if (seshs % 2 == 0 or seshs == 0):
                print (" Odd session begin.")
                time.sleep(rnd.random() * 0.01 + 0.07) # wait before next action
                pyautogui.moveTo(rnd.randint(1245,1255), rnd.randint(690,730), 0.43 + 0.151 * rnd.random() + 3/27 * rnd.random()) # move mouse to bank, sit at top left of GE.
                time.sleep(rnd.random() * 0.31 + 0.07) # wait before next action
                mouse.click()
                time.sleep(rnd.random() * 0.31 + 0.07) # wait before next action
                pyautogui.moveRel(rnd.randint(-10,10), rnd.randint(-10,14), rnd.random() * 0.43 + 0.9) #Move around from current spot
                pyautogui.moveRel(rnd.randint(-7,7), rnd.randint(-22,12), rnd.random() * 2/27 + 0.1327) #Move around from current spot
                #time.sleep(1.382 + 0.18 * rnd.random()) # sleep. 
                #pyautogui.moveTo(rnd.randint(1053,1058), rnd.randint(530,539), 0.3693 + 6/27 * rnd.random() + 3/27 * rnd.random()) # Move to bank
                #time.sleep(rnd.random() * 0.11 + 0.13)
                #mouse.click() # Click to open bank
                #print("Mouse position to open bank for sesh 1:", pyautogui.position()) # print position
                pyautogui.moveRel(rnd.randint(-1,1), rnd.randint(1,2), rnd.random() * 0.13 + 0.9) #Move around from current spot
                time.sleep(rnd.random() * 0.21 + 0.43)
                print ("Getting wood.")
                pyautogui.moveTo(rnd.randint(986, 1004), rnd.randint(166, 172), rnd.random() * 0.133 + 0.46) # move to wood
                time.sleep(rnd.random()* 0.173 + 0.21) #Sleep
                mouse.right_click() #open wood options now.
                time.sleep(0.181 * rnd.random() + 0.2) #sleep
                pyautogui.moveRel(rnd.randint(-12, 5), rnd.randint(100, 107), rnd.random() * 0.121 + 0.18) #move mouse down to quantity of ALL
                time.sleep(rnd.random() * 0.19 + 0.29)
                mouse.click() #Get wood
                time.sleep(rnd.random() * 0.19 + 0.29)
                # Moving to burn spot 1
                pyautogui.moveTo(rnd.randint(1504, 1522), rnd.randint(727, 733), rnd.random() * 0.133 + 0.26) # move to burn spot 1 !
                time.sleep(rnd.random() * 0.1 + 0.19)
                pyautogui.moveRel(rnd.randint(-1,1), rnd.randint(1,2), rnd.random() * 0.13 + 0.1) #Move around from current spot
                mouse.click()
                pyautogui.moveRel(rnd.randint(-20,40), rnd.randint(-100,-20), rnd.random() * 0.131 + 0.1) #Move around from current spot
                pyautogui.moveRel(rnd.randint(-32, 42), rnd.randint(6,12), rnd.random() * 0.131 + 0.1) # random movement
                pyautogui.moveRel(rnd.randint(-12, 12), rnd.randint(6,12), rnd.random() * 0.135 + 0.11) # random movement
                time.sleep(rnd.random() * 0.19 + 4.829)

            if (seshs > 0 and (seshs + 1) % 2 == 0): #sesh 2 sesh 2 sesh 2 sesh 2 sesh 2 sesh 2 sesh 2 sesh 2
                print ("Even session begin.")
                pyautogui.moveTo(rnd.randint(1196, 1208), rnd.randint(369,379), 0.43 + 0.5 * rnd.random() + 3/27 * rnd.random()) #move to bank after sesh 1
                time.sleep(rnd.random() * 0.2 + 0.3) # wait before next action, use .1 multiplier because we aren't moving mouse position. 
                mouse.click() # Open up bank
                print("Mouse position at banker to start sesh 2:", pyautogui.position()) # print position
                print ("Getting wood for the even sessions.")
                time.sleep(rnd.random() * .1 + 3.35)                 
                pyautogui.moveTo(rnd.randint(986, 1004), rnd.randint(166, 172), rnd.random() * 0.131 + 0.39) # move to wood
                time.sleep(rnd.random()* 0.0173 + 1.21) 
                mouse.right_click() #open wood options 
                time.sleep(0.1 * rnd.random() + 0.2) 
                pyautogui.moveRel(rnd.randint(-12, 5), rnd.randint(100, 107), rnd.random() * 0.1 + 0.133) #move mouse down to quantity of ALL
                time.sleep(rnd.random() * 0.1 + 0.19)
                mouse.click() #Get wood
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

            ## ~~~ Random mouse movement ~~~~ ####
            pyautogui.moveRel(rnd.randint(-10,9), rnd.randint(0,6), rnd.random() * 0.12 + 0.03) #Move around from current spot
            time.sleep(rnd.random() * 0.131 + 0.106) #Sleep
            pyautogui.moveRel(rnd.randint(-20,40), rnd.randint(-100,20), rnd.random() * 0.13 + 0.1) #Move around from current spot
            time.sleep(rnd.random() * 0.03 + 0.01) #Sleep
            pyautogui.moveRel(rnd.randint(-2, 12), rnd.randint(6,12), rnd.random() * 0.13 + 0.15) # random movement
            time.sleep(rnd.random() * 0.13 + 0.01) #Sleep
            ## ~~~ Random mouse movement ~~~~ ####

            # Time to burn logs, this portion is extensive...
            xpus = 1755
            ypus = 765
            for i in range (1, 23):
                pyautogui.moveTo(rnd.randint(1709,1720), rnd.randint(752, 768), rnd.random() * 0.03 + 0.197) #move to tinder box
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
            seshs = seshs + 1
            logsBurnt = logsBurnt + 20
            print ("This is batch number:", seshs, "with,", logsBurnt, "logs burnt.")
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