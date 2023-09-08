import tkinter as tk
import time
import threading
import pyautogui
import mouse
import sys
import random as rnd
from pynput.keyboard import Listener, KeyCode
from contextlib import redirect_stdout
from io import StringIO

# Import your functions here
from AFunctions import *

# Global variables
global running
global rounds
global Clickz
global rnum

ONOFF = KeyCode(char="1")
KEY = KeyCode(char='2')

rounds = 0
Clickz = 0
running = False
rnum = rnd.randint(80, 99)

# Create a list to store messages for the GUI
gui_messages = []

# Redirect stdout to a buffer
console_output = StringIO()
sys.stdout = console_output

# Function to start/stop the bot
def start_bot():
    global running
    if running:
        running = False
        print_to_gui("Bot Stopped")
    else:
        running = True
        print_to_gui("Bot Started")

# Function to update the Text widget with console output
def update_textbox():
    text_widget.delete('1.0', tk.END)
    for message in gui_messages:
        text_widget.insert(tk.END, message + '\n')
    text_widget.see(tk.END)  # Scroll to the end of the text

    # Schedule the next update
    root.after(1000, update_textbox)  # Update every 1000 milliseconds (1 second)

# Function to print to the GUI text widget
def print_to_gui(text):
    gui_messages.append(text)
    text_widget.insert(tk.END, text + '\n')
    text_widget.see(tk.END)  # Scroll to the end of the text

# Function to run the bot logic
def run_bot():
    while True:
        if running:
            global Clickz
            global rnum
            if Clickz == 0:
                print_to_gui("Let's RIDE!")

            time.sleep(rnd.random() * 3/27 + 0.43)
            mouse.click()
            time.sleep(rnd.random() * 3/27 + 0.58)
            Clickz = Clickz + 1

            if (Clickz % rnum == 0):
                time.sleep(rnd.randint(1, 3) * rnd.random())
                print_to_gui(f"Time for a break! Rnum value is currently: {rnum}")

            if (Clickz % rnd.randint(28, 39) == 0):
                time.sleep(rnd.random() * 0.1)

        time.sleep(1)  # Adjust the sleep interval as needed

# Function to listen for keypress events
def on_keypress(key):
    if key == ONOFF:
        start_bot()
        print_to_gui("Bot is running")

# Create the main GUI window
root = tk.Tk()
root.title("Bot GUI")

# Create a Text widget to display console output
text_widget = tk.Text(root)
text_widget.pack(fill=tk.BOTH, expand=True)

# Create a label to display the bot's status
status_label = tk.Label(root, text="Stopped")
status_label.pack()

# Add a welcome message and display the current time when the GUI boots up
welcome_message = "Welcome to the Bot GUI!\n"
current_time = time.strftime("%Y-%m-%d %H:%M:%S")
welcome_and_time = welcome_message + "Current Time: " + current_time + "\n\n"
text_widget.insert(tk.END, welcome_and_time)

# ... (Your other functions and code)

# Create threads for the bot and the console updater
bot_thread = threading.Thread(target=run_bot)
bot_thread.start()

# Start the initial update of the GUI
update_textbox()

# Create a listener for keypress events
with Listener(on_press=on_keypress) as listener:
    # Run the main GUI loop
    root.mainloop()

# Stop the listener after the GUI loop exits
listener.stop()
listener.join()