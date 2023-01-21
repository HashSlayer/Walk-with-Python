import threading
import pyautogui
import time
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import win32api, win32con

KEY = KeyCode(char ='2')
ONOFF = KeyCode(char="1")

global running
running = False
cspeed = 1 #click speed
mouse = Controller()

def clicker():
    while True:
        if running:
            print(pyautogui.position())
        time.sleep(3) #Change this value to change how often the pixel location is printed
def togglebot(key):
    if key == ONOFF:
        global running
        print ("Program PXL is on:", not running)
        running = not running
    elif key == KEY: 
        print ("Kill switch acitaved; Pixel locator is now off.")
        running = False
        exit() # This will end the program entirely

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=togglebot) as listner:
    listner.join()