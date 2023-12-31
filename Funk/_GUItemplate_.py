import sys
import os
import threading
import random as rnd
from pynput.keyboard import Listener, KeyCode, Key
import tkinter as tk
from tkinter import font as tkFont
from datetime import datetime
# KEEP THESE IN
#Get the directory of the current script
current_script_dir = os.path.dirname(__file__)
# Get the parent directory of the current script
parent_dir = os.path.abspath(os.path.join(current_script_dir, '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)
# We can now import from the parent directory
from AFunctions import *
from A2Functions import *
from Conffeti import *

# Global variables
running = False
running_lock = threading.Lock()
bot_thread = None
ClickCount, maxClicks, Ct, Xt, = 1, 420, 1, 0.1

# Define your special keys
ONOFF = Key.alt_l  # Left Alt key for toggling on/off
KEY = Key.alt_r  # Right Alt key to exit the program

welcome()

# =======================================================================================================================
# Functions
# =======================================================================================================================

def SimulatedPause():
    global ClickCount, SleepWeight
    if (rnd.random() > 0.8889):
        sleepy(.1, 1)
        if (rnd.random() > 0.68):
            sleepy(.1, 1)

# [~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GUI Class ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]
class GGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("@5MEkailO's OSWS Bot")
        self.setup_gui()
        self.apply_style()
        self.create_top_frame()
        self.create_text_box()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind("<Configure>", self.on_resize)
        self.click_tracker = ClickTracker(self.append_message, self.canvas)
        self.random_sleep_enabled = False
        self.click_tracker_thread = None

    def setup_gui(self):
        self.background_color_start = "#FF6B6B"  # Vibrant pink for gradient start
        self.background_color_end = "#4D96FF"    # Bright yellow for gradient end
        self.create_gradient_background()

    def apply_style(self):
        # New color palette and font
        self.bg_color = "#FF6B6B"  # Vibrant pink
        self.button_color = "#FF6B6B"  # Electric blue 4D96FF
        self.text_color = "#99E1A2"  # Fresh green
        self.hover_color = "#F55C47"  # Fiery orange for button hover
        self.custom_font = tkFont.Font(family="Consolas", size=13, weight="bold")
        self.root.configure(bg=self.bg_color)
    
    def create_gradient(self, canvas, color1, color2, width, height):
        for i in range(height):
            r1, g1, b1 = canvas.winfo_rgb(color1)
            r2, g2, b2 = canvas.winfo_rgb(color2)
            r = (r1 + int((r2 - r1) * i / height)) & 0xff00
            g = (g1 + int((g2 - g1) * i / height)) & 0xff00
            b = (b1 + int((b2 - b1) * i / height)) & 0xff00
            color = f'#{r:04x}{g:04x}{b:04x}'
            canvas.create_line(0, i, width, i, fill=color)

    def create_gradient_background(self):
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", self.on_resize)
        self.on_resize(None)  # Initial call to set the gradient

    def apply_gradient(self, canvas, color1, color2, width, height):
        for i in range(height):
            # Adjust the blend factor for a more extreme gradient
            blend_factor = (i / height) ** 2  # Example: quadratic blend for more abrupt change
            r1, g1, b1 = canvas.winfo_rgb(color1)
            r2, g2, b2 = canvas.winfo_rgb(color2)
            r = (r1 + int((r2 - r1) * blend_factor)) & 0xff00
            g = (g1 + int((g2 - g1) * blend_factor)) & 0xff00
            b = (b1 + int((b2 - b1) * blend_factor)) & 0xff00
            color = f'#{r:04x}{g:04x}{b:04x}'
            canvas.create_line(0, i, width, i, fill=color)

    def start_confetti_animation(self):
        startConfetti(self.canvas)

    def track_clicks(self):
        if not self.click_tracking_enabled:
            self.start_click_tracking()
        else:
            self.stop_click_tracking()

    def start_click_tracking(self):
        if not self.click_tracker.tracking:
            self.click_tracker_thread = threading.Thread(target=self.click_tracker.run)
            self.click_tracker_thread.daemon = True
            self.click_tracker_thread.start()
        else:
        # If the thread is already running, just enable click processing
            self.click_tracker.process_clicks = True
        self.click_tracking_enabled = True
        self.toggle_button.config(text="Track Clicks: ON", bg="#2ECC73")

    def stop_click_tracking(self):
        # Just disable click processing without stopping the thread
        self.click_tracker.process_clicks = False
        self.click_tracking_enabled = False
        self.toggle_button.config(text="Track Clicks: OFF", bg="#FF6B6B")

    def create_top_frame(self):
        # Create the top frame
        top_frame = tk.Frame(self.canvas, bg=self.bg_color)
        top_frame.pack(padx=10, pady=10)
        # Date Label
        self.date_label = tk.Label(top_frame, text="", bg="#FF6B6B", fg='#97E469', font=("Consolas", 13, "bold"), relief=tk.RAISED, borderwidth=1)
        self.date_label.pack(side="left", padx=(80, 2))  # Small separation between date and time
        # Time Label
        self.time_label = tk.Label(top_frame, text="", bg="#FF6B6B", fg='#97E469', font=("Consolas", 13, "bold"), relief=tk.RAISED, borderwidth=1)
        self.time_label.pack(side="left", padx=2)
        # Label style with border
        # Updated style for labels and entries
        label_style = {"bg": "#FF6B6B", "fg": "#97E469", "font": self.custom_font, "relief": tk.FLAT, "borderwidth": 0}
        entry_style = {"bg": "#FF6B6B", "fg": "#97E469", "font": self.custom_font, "relief": tk.SUNKEN, "borderwidth": 1}

        # Click Every (Ct) Label and Entry
        tk.Label(top_frame, text="Click Every:", **label_style).pack(side=tk.LEFT, padx=(10, 0))
        self.ct_entry = tk.Entry(top_frame, width=5, **entry_style)
        self.ct_entry.pack(side=tk.LEFT, padx=(3, 10))
        self.ct_entry.insert(0, "1")  # Default value
        # Random Multiplier (Xt) Label and Entry
        tk.Label(top_frame, text="(+/-):", **label_style).pack(side=tk.LEFT, padx=(10, 0))
        self.xt_entry = tk.Entry(top_frame, width=5, **entry_style)
        self.xt_entry.pack(side=tk.LEFT, padx=(3, 10))
        self.xt_entry.insert(0, "0.5")  # Default value
        # Max Clicks Label and Entry
        tk.Label(top_frame, text="Max Clicks:", **label_style).pack(side=tk.LEFT, padx=(10, 0))
        self.max_clicks_entry = tk.Entry(top_frame, width=7, **entry_style)
        self.max_clicks_entry.pack(side=tk.LEFT, padx=(3, 10))
        self.max_clicks_entry.insert(0, "420")  # Default value

        # Kill Button
        self.kill_button = tk.Button(top_frame, text="KILL", command=self.kill_bot, bg=self.button_color, fg='#97E469', font=self.custom_font, activebackground=self.hover_color, relief=tk.RAISED, borderwidth=3)
        self.kill_button.pack(side=tk.RIGHT, padx=9)
        # Start / Stop Button
        self.start_button = tk.Button(top_frame, text="  Start / Stop  ", command=self.toggle_bot, bg=self.button_color, fg='#97E469', font=self.custom_font, activebackground='#C8F6AD', relief=tk.RAISED, borderwidth=3)
        self.start_button.pack(side=tk.RIGHT, padx=9)
        # Track Clicks Toggle Switch
        self.click_tracking_enabled = False  # Initialize as False
        self.toggle_button = tk.Button(top_frame, text="Track Clicks", command=self.track_clicks, bg=self.button_color, fg='#97E469', font=self.custom_font, activebackground='#C8F6AD', relief=tk.RAISED, borderwidth=3)
        self.toggle_button.pack(side=tk.LEFT, padx=9)
        self.update_time()

    def update_time(self):
        # Get current date and time with milliseconds
        now = datetime.now()
        date_str = now.strftime(" %B %d, %Y ")
        time_str = now.strftime(" %H:%M:%S") + ".{:03d} ".format(now.microsecond // 1000)
        self.date_label.config(text=date_str)
        self.time_label.config(text=time_str)
        self.root.after(50, self.update_time)  # Update the time more frequently

    def create_text_box(self):
        self.text_box = tk.Text(self.canvas, wrap="word", bg="#FFE062", fg="#217BFF", font=("Consolas", 13), insertbackground="#5BCB77", relief="sunken", borderwidth=2)
        self.text_box.pack(fill=tk.BOTH, expand=True, padx=8, pady=10)
        #Remeber, bg is the background color, fg is the text color, insertbackground is the color of the cursor

    def on_resize(self, event):
        if event:  # Check if event is None
            width, height = event.width, event.height
        else:
            width, height = self.root.winfo_reqwidth(), self.root.winfo_reqheight()
        self.canvas.delete("gradient")
        self.create_gradient(self.canvas, self.background_color_start, self.background_color_end, width, height)

    def kill_bot(self):
        self.kill_button.config(text="KILLED", bg="#FF6B6B", fg='#97E469')
        #apply conffeti
        self.start_confetti_animation()
        kAltright()
        self.click_tracking_enabled = False

    def append_message(self, message):
        self.text_box.insert(tk.END, message + '\n')
        self.text_box.see(tk.END)

    def toggle_bot(self):
        global running, bot_thread
        with running_lock:
            if not running:
                self.append_message("Starting in 2, 1..")
                print("Starting in 2")
                sleepy(1, 0, 0)
                print("Starting in 1")
                sleepy(1, 0, 0)
                print("Turning running to", not running)
                running = True
                self.start_button.config(text="       STOP       ", bg="#FF6B6B", fg='#97E469')  # Red background, white font
                if bot_thread is None or not bot_thread.is_alive():
                    bot_thread = threading.Thread(target=lambda: walker(self))
                    bot_thread.start()
            else:
                running = False
                self.start_button.config(text="     START     ", bg="#09C159", fg='#97E469')  # Green background, white font
                self.append_message("Bot Paused")

    def run(self):
        self.root.mainloop()

#  =========================================== | End of GUI Class | ===========================================

def walker(gui):
    while True:
        if running:
            global ClickCount, maxClicks, Ct, Xt

            # Retrieve values from entry widgets
            try:
                maxClicks = int(gui.max_clicks_entry.get())
                Ct = float(gui.ct_entry.get())
                Ct = max(0, Ct)  # Ensure Ct is non-negative
                Xt = float(gui.xt_entry.get())
                Xt = max(0, Xt)  # Ensure Xt is non-negative
            except ValueError:
                print("Invalid Ct or Xt value")
                break

            if not running:
                break

            if ClickCount == 1:
                print("Let's Click;", maxClicks, "times.")

            # Sleep logic
            sleepy(Ct, Xt/2, Xt/2)  # Sleeps for up to 1 min 30 seconds naturally
            if not running:
                break

            # Click action
            clx()
            ClickCount += 1

            # Confetti animation and messages
            if (ClickCount - 1) % 100 == 0:
                gui.append_message("❤️==================100========================❤️")
                gui.start_confetti_animation()

            if ClickCount % maxClicks == 0:
                gui.start_confetti_animation()
                gui.append_message(f"You have reached the goal of {ClickCount} clicks!")
                print("Goal Reached!")
                if running:
                    gui.toggle_bot()  # Toggle bot off when goal is reached
                break
def stop_bot():
    global running
    running = False

def togglebot(key, gui):
    global running, bot_thread
    if key == ONOFF:
        with running_lock:
            if running:
                running = False
                print("Bot Paused")  # Console message
                gui.append_message("Bot Paused")  # GUI message
                gui.start_button.config(text="       STOP       ", bg="#FF6B6B", fg='#97E469')  # Red background, white font
            else:
                running = True
                print("Bot started")  # Console message
                gui.append_message("Bot Started")  # GUI message
                gui.start_button.config(text="     START     ", bg="#09C159", fg='#97E469')  # Green background, white font
                if bot_thread is None or not bot_thread.is_alive():
                    bot_thread = threading.Thread(target=lambda: walker(gui))
                    bot_thread.start()

    elif key == KEY:
        print("Kill switch activated")
        gui.append_message("You killed it!")
        gui.start_confetti_animation()
        stop_bot()
        running = False
        sys.exit()

# Start the GUI and bot
if __name__ == "__main__":
    gui = GGui()
    listener_thread = threading.Thread(target=lambda: Listener(on_press=lambda key: togglebot(key, gui)).start())
    listener_thread.start()
    gui.run()
    listener_thread.join()

# ~#~ End Script ~#~