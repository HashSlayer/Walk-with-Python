import threading
import pyautogui
import time
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import win32api, win32con

KEY = KeyCode(char ='`')
ONOFF = KeyCode(char="1")

global running
running = False
cspeed = 1 #click speed
mouse = Controller()
1
def clicker():
    while True:
        if running:
            print(pyautogui.position())
        time.sleep(1) #Change this value to change how often the pixel location is printed


    
def togglebot(key):
    if key == ONOFF:
        global running
        running = not running
        print ("Pixel locator is on:", not running)
    elif key == KEY: 
        print ("Kill switch acitaved; Pixel locator is now off.")
        running = False
        # End the program entirely
        exit()

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=togglebot) as listner:
    listner.join()