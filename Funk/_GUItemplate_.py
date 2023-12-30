import time
import sys
import os
import threading
import random as rnd
from pynput.keyboard import Listener, KeyCode
# Get the directory of the current script
current_script_dir = os.path.dirname(__file__)
# Get the parent directory of the current script
parent_dir = os.path.abspath(os.path.join(current_script_dir, '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)
from AFunctions import *
from A2Functions import *
import tkinter as tk
from tkinter import font as tkFont
from datetime import datetime
from Conffeti import *


global running, ClickCount, maxClicks, bot_thread

ONOFF = KeyCode(char="1")
KEY = KeyCode(char ='2')

running_lock = threading.Lock()
bot_thread = None
running = False
ClickCount = 1
maxClicks = 100 

welcome()

#=======================================================================================================================


#=======================================================================================================================

# GUI Class
class AutoClickerGUI:
    # ... existing methods ...
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("OSWS Walker")
        self.apply_style()
        # Create the background Canvas
        self.create_background_canvas()
        # Create GUI components
        self.create_top_frame()
        self.create_text_box()

    def create_background_canvas(self):
        self.bg_canvas = tk.Canvas(self.root, bg=self.bg_color, highlightthickness=0)
        self.bg_canvas.place(relwidth=1, relheight=1)  # Cover the entire window

    def start_confetti_animation(self):
        startConfetti(self.bg_canvas)

    def apply_style(self):
        # Enhanced color palette
        self.bg_color = "#9174BB"  # Dark blue-gray
        self.button_color = "#2ECC71"  # Emerald green
        self.text_color = "#ECF0F1"  # Off-white
        self.hover_color = "#E74C3C"  # Soft red
        # Stylish font
        self.custom_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        # Set root window background color
        self.root.configure(bg=self.bg_color)

    def create_top_frame(self):
        # Create the top frame
        top_frame = tk.Frame(self.root, bg=self.bg_color)
        top_frame.pack(padx=10, pady=10)
        # Time Label
        self.time_label = tk.Label(top_frame, text="", bg="#FFD30D" , fg='#FF780D', font=("Consolas", 13, "bold"), relief=tk.RAISED, borderwidth= 3) #FF780D is Orange
        self.time_label.pack(side="left", padx=80, pady=10)
        # Kill Button
        self.kill_button = tk.Button(top_frame, text="Kill", command=self.kill_bot, bg='#FF6B6B', fg='#ECF0F1', font=self.custom_font, activebackground=self.hover_color, relief=tk.RAISED, borderwidth=3)
        self.kill_button.pack(side=tk.RIGHT, padx=5)
        self.update_time()
        # Start / Stop Button
        self.start_button = tk.Button(top_frame, text="Start / Stop", command=self.toggle_bot, bg=self.button_color, fg='#FF780D', font=self.custom_font, activebackground='#28B065', relief=tk.RAISED, borderwidth=3)
        self.start_button.pack(side=tk.RIGHT, padx=5)
        # Max Items Entry
        tk.Label(top_frame, text="Max Items:", bg=self.bg_color, fg=self.text_color, font=self.custom_font).pack(side=tk.LEFT, padx=(10, 0))
        self.max_items_entry = tk.Entry(top_frame, width=7, font=self.custom_font)
        self.max_items_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.max_items_entry.insert(0, "100")  # Default value    

    def create_text_box(self):
        self.text_box = tk.Text(self.root, height=10, bg=self.bg_color, fg=self.text_color, font=self.custom_font, relief=tk.RIDGE, borderwidth=3)
        self.text_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def update_time(self):
        now = datetime.now().strftime(" %H:%M:%S ")
        self.time_label.config(text=now)
        self.root.after(1000, self.update_time)

    def kill_bot(self):
        k2()

    def append_message(self, message):
        self.text_box.insert(tk.END, message + '\n')
        self.text_box.see(tk.END)

    def toggle_bot(self):
        self.append_message("Starting in 3, 2, 1..")
        print ("Starting in 3")
        sleepy(1, 0, 0)
        print ("Starting in 2")
        sleepy(1, 0, 0)
        print ("Starting in 1")
        sleepy(1, 0, 0)
        print ("Turning running to", not running)
        k1()

    def run(self):
        self.root.mainloop()


def walker(gui):
    while True:
        if running:
            global maxClicks #ADD VARIABLE HERE

            # Retrieve values from entry widgets
            try:
                maxClicks = int(gui.max_items_entry.get())
                # ... [retrieve other values] ...
            except ValueError:
                print("Invalid input value")
                break

            if (False): #Kill the program after X Clicks
                gui.append_message(f"You have reached the goal!")
                gui.start_confetti_animation()
                stop_bot()
                # END OF THE TEST WALKER SCRIPT> REPLACE 

def stop_bot():
    global running, bot_thread
    with running_lock:
        running = False
    if bot_thread is not None:
        bot_thread.join()

def togglebot(key, gui):
    global running, bot_thread
    if key == ONOFF:
        with running_lock:
            if running:
                running = False
                print("Bot Paused")  # Console message
                gui.append_message("Bot Paused")  # GUI message
            else:
                running = True
                print("Bot started")  # Console message
                gui.append_message("Bot Started")  # GUI message
                if bot_thread is None or not bot_thread.is_alive():
                    bot_thread = threading.Thread(target=lambda: walker(gui))
                    bot_thread.start()

    elif key == KEY:
        print("Kill switch activated")
        gui.append_message("You killed it!")
        gui.start_confetti_animation()
        stop_bot()
        sys.exit()

# Start the GUI and bot
if __name__ == "__main__":
    gui = AutoClickerGUI()
    listener_thread = threading.Thread(target=lambda: Listener(on_press=lambda key: togglebot(key, gui)).start())
    listener_thread.start()
    gui.run()
    listener_thread.join()

