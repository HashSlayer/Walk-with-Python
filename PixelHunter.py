import threading
import pyautogui
import time
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode


ONOFF = KeyCode(char="`")
KEY = KeyCode(char ='?')
#We are going to spice this up a bit using another KeyCode to toggle the bot to print the pixel location of the mouse.
#We will use the 3 key to toggle the bot to print the pixel location of the mouse.
SHOT = KeyCode(char="3")

global running
running = False
global mousex
global mousey
global count

count = 0

print ( " Lets hunt some pixels! ")

mouse = Controller()

def clicker():
    while True:
        if running:
            global mousex
            global mousey
            global count
            #print(pyautogui.position())
        #time.sleep(1) #Change this value to change how often the pixel location is printed
            print("Count:", count, "...")
            print(mouse.position)
            #Extrapolate the X value from the position tuple, and assign it to mousex
            mousex = mouse.position[0]
            #Extrapolate the Y value from the position tuple, and assign it to mousey
            mousey = mouse.position[1]
            print("pyautogui.moveTo(rnd.randint(", (mousex - 5), ",", (mousex + 5), "), rnd.randint(", mousey - 5, ",", mousey + 5,"), rnd.random() * 0.1 + 0.3)")
            print(" ")
            time.sleep(1)
            print(" --------------------------------------------------------------------------------------------------------------------------------------------")
            count = count + 1




    
def togglebot(key):
    if key == ONOFF:
        global running
        running = not running
        print ("Pixel locator is on:", running)
    elif key == KEY: 
        print ("Kill switch acitaved; Pixel locator is now off.")
        running = False
        # End the program entirely
        exit()

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=togglebot) as listner:
    listner.join()