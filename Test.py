#import all the modules used in the other files including AFuntions.py
import time
import sys
import threading
import pyautogui
import mouse
import random as rnd
from pynput.keyboard import Listener, KeyCode
from AFunctions import *

#Using AFunctions.oy call the welcome function

welcome()
time.sleep(3)

#create a for loop that runs the slot functions 10 times in a row

for i in range(9):
    Slot1()
    Slot2()
    Slot3()
    Slot4()



