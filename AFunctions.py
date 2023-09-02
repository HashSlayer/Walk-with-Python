import time
import sys
import threading
import pyautogui
import mouse
import random as rnd
from pynput.keyboard import Listener, KeyCode

Welcome = "Welcome to Old School Walk Scape"

# Create functions for tasks that the bots share in common.
# create a function that will push down the up key for 4 seconds, then release it.
#Define a function that welcome the player to the program "Old School Walk Scape."

def welcome():
    print (Welcome)
    time.sleep(0.5 * rnd.random() + 0.1)
    print ("press \ to exit the program")
    print ("Enjoy your walk!")


def upkey():
    pyautogui.keyDown('up')
    time.sleep(0.003 * rnd.random() + 0.01)
    time.sleep(3.5)
    pyautogui.keyUp('up')
    time.sleep(0.003 * rnd.random() + 0.01)

#Define downkey function

def downkey():
    pyautogui.keyDown('down')
    time.sleep(0.003 * rnd.random() + 0.01)
    time.sleep(3.5)
    pyautogui.keyUp('down')
    time.sleep(0.003 * rnd.random() + 0.01)

#Define a function that will push down the left key for 3 seconds, then release it.

def leftkey():
    pyautogui.keyDown('left')
    time.sleep(0.0003 * rnd.random() + 0.01)
    time.sleep(3)
    pyautogui.keyUp('left')
    time.sleep(0.0003 * rnd.random() + 0.01)

#Define a function that will click on the map

def Compass():
    time.sleep(0.0003 * rnd.random() + 0.01)
    pyautogui.moveTo(rnd.randint(1716, 1729), rnd.randint(38, 48), rnd.random() * 0.181 + 0.81) #move to map
    time.sleep(0.0003 * rnd.random() + 0.1)
    mouse.click() #click map
    time.sleep(0.03 * rnd.random() + 0.1)



#Define a function that scrolls the mouse wheel down by 20 clicks, spaced out like a human would.

def Zoomout():
    for i in range (1, 18):
        pyautogui.scroll(-1)
        time.sleep(0.03 * rnd.random() + 0.39)

#Define a function that scrolls the mouse wheel up by 20 clicks, spaced out like a human would.

def Zoomin():
    for i in range (1, 18):
        pyautogui.scroll(1)
        time.sleep(0.03 * rnd.random() + 0.39)

# Get into birds eye view
def Birdseye():
    Compass()
    time.sleep(0.0003 * rnd.random() + 0.01)
    Zoomout()
    time.sleep(0.0003 * rnd.random() + 0.01)
    upkey()
    time.sleep(0.0003 * rnd.random() + 0.01)

def Flatview():
    Compass()
    time.sleep(0.0003 * rnd.random() + 0.01)
    Zoomin()
    time.sleep(0.0003 * rnd.random() + 0.01)
    downkey()
    time.sleep(0.0003 * rnd.random() + 0.01)



#Define a function that makes random and realistic mouse movements totaling about 2 seconds. + or - 0.2 seconds.
def Notbotting():
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep
    pyautogui.moveTo(rnd.randint(700,980), rnd.randint(220,480), 0.33 + 0.01 * rnd.random() + 3/27 * rnd.random())
    pyautogui.moveRel(rnd.randint(-40, 74), rnd.randint(-99,12), 0.33 + 0.01 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep
    pyautogui.moveRel(rnd.randint(-40, 74), rnd.randint(-200,6), 0.33 + rnd.random() * 3/27) # random movement
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random())

#Define another Notbotting function that makes random and realistic mouse movements totaling about 3 seconds. + or - 0.2 seconds, with a different range of movement.

def Notbotting2():
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep
    pyautogui.moveTo(rnd.randint(300,1180), rnd.randint(300,780), 0.60 + 0.01 * rnd.random() + 3/27 * rnd.random())
    pyautogui.moveRel(rnd.randint(-400, 740), rnd.randint(-99,12), 0.63 + 0.01 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep
    pyautogui.moveRel(rnd.randint(-400, 740), rnd.randint(-20,20), 0.63 + rnd.random() * 3/27) # random movement
    pyautogui.moveRel(rnd.randint(-10,10), rnd.randint(-4,14), rnd.random() * 0.03 + 0.02) #Move around from current spot
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random())

def Notbotting3():
    pyautogui.moveRel(rnd.randint(-10,9), rnd.randint(0,6), rnd.random() * 0.12 + 0.03) #Move around from current spot
    time.sleep(rnd.random() * 0.131 + 0.106) #Sleep
    pyautogui.moveRel(rnd.randint(-20,40), rnd.randint(-100,20), rnd.random() * 0.13 + 0.1) #Move around from current spot
    time.sleep(rnd.random() * 0.03 + 0.01) #Sleep
    pyautogui.moveRel(rnd.randint(-2, 12), rnd.randint(6,12), rnd.random() * 0.13 + 0.15) # random movement
    time.sleep(rnd.random() * 0.13 + 0.01) #Sleep






#Banking functions:
#Define a function that will move the mouse to a random spot between X= 990 and 1008, Y= 817 and 830, then click, including human like delays, and movements between clicks.
#This will deposit all items in the inventory.

def Deposit():
    time.sleep(0.13 + 0.03 * rnd.random() + rnd.random())
    pyautogui.moveTo(rnd.randint(990, 1008), rnd.randint(817, 830), 0.5 + 0.1 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.63 + 0.1 * rnd.random() + rnd.random())
    mouse.click()
    pyautogui.moveRel(rnd.randint(-40, 70), rnd.randint(-2,2), 0.33 + 0.01 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep

#Define a function that drops down to get X amount of items.

def Getitems():
    time.sleep((rnd.random() * 13/120 + 0.05)) # Sleep
    mouse.right_click() #open item options         
    time.sleep((0.12 + rnd.random() * 0.15)) #sleep
    pyautogui.moveRel(rnd.randint(-21,21), rnd.randint(71,73), rnd.random() *0.12 +0.13) #move mouse down to quantity of X
    time.sleep((rnd.random() * 0.087 + rnd.random() * 0.23 + 0.15)) #sleep
    mouse.click() # Get X amount of items
    time.sleep((0.01 + rnd.random() * 0.01)) #Short Sleep

def Getall():
    time.sleep(rnd.random()* 0.173 + 0.21) #Sleep
    mouse.right_click() #open wood options now.
    time.sleep(0.181 * rnd.random() + 0.2) #sleep
    pyautogui.moveRel(rnd.randint(-12, 5), rnd.randint(100, 107), rnd.random() * 0.121 + 0.18) #move mouse down to quantity of ALL
    time.sleep(rnd.random() * 0.19 + 0.29)
    mouse.click() #Get wood
    time.sleep(rnd.random() * 0.19 + 0.29)

#To move down we increase the Y value; to move down one item slot in the bank, we increase the Y value by 35 or 38.
#Define a function that moves the mouse to an item in the bank

def Slot1():
    time.sleep(0.01 + 0.01 * rnd.random() + rnd.random()) #sleep
    pyautogui.moveTo(rnd.randint(977, 983), rnd.randint(140, 150), 0.2 + 0.1 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep

#define slot 2 which is 35 pixels down from slot 1 currently wood

def Slot2():
    time.sleep(0.01 + 0.01 * rnd.random() + rnd.random()) #sleep
    pyautogui.moveTo(rnd.randint(977, 983), rnd.randint(175, 185), 0.2 + 0.1 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep

#define slot 3 which is 35 pixels down from slot 2

def Slot3():
    time.sleep(0.01 + 0.01 * rnd.random() + rnd.random()) #sleep
    pyautogui.moveTo(rnd.randint(977, 983), rnd.randint(210, 220), 0.2 + 0.1 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep

#define slot 4 which is 35 pixels down from slot 3

def Slot4():
    time.sleep(0.01 + 0.01 * rnd.random() + rnd.random()) #sleep
    pyautogui.moveTo(rnd.randint(977, 983), rnd.randint(245, 255), 0.2 + 0.1 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep

#define a function that moves the mouse to the left by 35 pixels in relation to the current position of the mouse.

def Left():
    time.sleep(0.01 + 0.01 * rnd.random() + rnd.random()) #sleep
    pyautogui.moveRel(rnd.randint(-36, -34), rnd.randint(-2,2), 0.3 + 0.1 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep

