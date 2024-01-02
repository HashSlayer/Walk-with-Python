import pyautogui as pag
import time
import random as rnd
from .Movement import bezierMove
from .MainFunctions import click, sleep


def Deposit():
    sleep(.1, 1)
    bezierMove(rnd.randint(990, 1008), rnd.randint(817, 830), 0.3 + 0.1 * rnd.random() + 3/27 * rnd.random())
    #50/50 if statement to move to the same spot with closer X and Y values
    if (rnd.random() > 0.4):
        bezierMove(rnd.randint(994, 1007), rnd.randint(819, 827), 0.08 + 0.01 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.1 + 0.1 * rnd.random() + 0.1 * rnd.random())
    click()
    pag.moveRel(rnd.randint(-4, 3), rnd.randint(-2,2), 0.01 + 0.01 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.07 + 0.01 * rnd.random()) #sleep

#Define a function that drops down to get X amount of items.

def Getitems():
    time.sleep((rnd.random() * 0.01 + 0.05)) # Sleep
    pag.rightClick #open item options         
    time.sleep((0.12 + rnd.random() * 0.15)) #sleep
    if (rnd.random() > 0.619):
        pag.moveRel(rnd.randint(-21,11), rnd.randint(71,73), rnd.random() *0.12 +0.13) #move mouse down to quantity of X
    else:
        pag.moveRel(rnd.randint(-21, 1), rnd.randint(71, 73), rnd.random() * 0.121 + 0.13)
    time.sleep((rnd.random() * 0.087 + rnd.random() * 0.23 + 0.15)) #sleep
    click() # Get X amount of items
    time.sleep((0.01 + rnd.random() * 0.01)) #Short Sleep

     # Copy the Getitems() function with this line: pag.moveRel(rnd.randint(-30, 17), rnd.randint(101, 114), yrt * 0.12 + 0.23) #move mouse down to quantity of all


def Getall():
    time.sleep(rnd.random()* 0.173 + 0.21) #Sleep
    pag.rightClick  #open wood options now.
    time.sleep(0.181 * rnd.random() + 0.2) #sleep
    if (rnd.random() > 0.4):
        pag.moveRel(rnd.randint(-19, 12), rnd.randint(100, 112), rnd.random() * 0.121 + 0.25) #move mouse down to quantity of ALL
    else:
        pag.moveRel(rnd.randint(-19, 5), rnd.randint(103, 109), rnd.random() * 0.121 + 0.28)
    time.sleep(rnd.random() * 0.19 + 0.29)
    click() #Get wood
    time.sleep(rnd.random() * 0.19 + 0.29)

#To move down we increase the Y value; to move down one item slot in the bank, we increase the Y value by 35 or 38.
#Define a function that moves the mouse to an item in the bank

def Slot1():
    time.sleep(0.1 + 0.01 * rnd.random() + rnd.random()) #sleep
    bezierMove(rnd.randint(977, 983), rnd.randint(140, 150), 0.2 + 0.2 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep

#define slot 2 which is 35 pixels down from slot 1 currently wood

def Slot2():
    time.sleep(0.1 + 0.01 * rnd.random() + rnd.random()) #sleep
    bezierMove(rnd.randint(977, 983), rnd.randint(175, 185), 0.23 + 0.2 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep

#define slot 3 which is 35 pixels down from slot 2

def Slot3():
    time.sleep(0.1 + 0.01 * rnd.random() + rnd.random()) #sleep
    bezierMove(rnd.randint(977, 983), rnd.randint(210, 220), 0.2 + 0.2 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep

#define slot 4 which is 35 pixels down from slot 3

def Slot4():
    time.sleep(0.1 + 0.01 * rnd.random() + rnd.random()) #sleep
    bezierMove(rnd.randint(977, 983), rnd.randint(245, 255), 0.2 + 0.2 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep

#define slot 5 which is 35 pixels down from slot 4

def Slot5():
    time.sleep(0.1 + 0.01 * rnd.random() + rnd.random()) #sleep
    bezierMove(rnd.randint(977, 983), rnd.randint(280, 290), 0.2 + 0.1 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep

#define a function that moves the mouse to the left by 35 pixels in relation to the current position of the mouse.

def Left35():
    time.sleep(0.1 + 0.01 * rnd.random() + rnd.random()) #sleep
    pag.moveRel(rnd.randint(-34, -36), rnd.randint(-2,2), 0.3 + 0.1 * rnd.random() + 3/27 * rnd.random())
    time.sleep(0.13 + 0.01 * rnd.random() + 3/27 * rnd.random()) #sleep

def Xbank():
    time.sleep(0.1 + 0.01 * rnd.random() + rnd.random()) #sleep
    bezierMove(rnd.randint(1040, 1044), rnd.randint(68, 70), rnd.random() * 0.1 + 0.24) # X of the bank
    time.sleep(0.01 + rnd.random() *0.198)
    click() #exit bank
    pag.moveRel(rnd.randint(-20, 12), rnd.randint(-6,12), rnd.random() * 0.1 + 0.04) # random movement

