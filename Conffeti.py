import random
import time
import tkinter as tk
from tkinter import font as tkFont
from pynput import mouse

def create_confetti(canvas):
    confetti = []
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    for _ in range(random.randint(69, 420)):  # Create a random number of confetti pieces
        x, y = random.randint(0, canvas_width), random.randint(0, canvas_height)
        confetti.append(canvas.create_oval(x, y, x+5, y+5, fill=random.choice(['red', 'blue', 'green', 'yellow', 'pink', 'purple', 'orange'])))
    return confetti

def update_confetti(canvas, confetti, start_time, duration=2):
    current_time = time.time()
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    if current_time - start_time < duration:  # Run the animation for the specified duration
        for item in confetti:
            x_move = random.randint(-5, 5)
            y_move = random.randint(-5, 5)
            canvas.move(item, x_move, y_move)
            # Ensure confetti stays within canvas bounds
            coords = canvas.coords(item)
            if coords[2] > canvas_width or coords[0] < 0:
                canvas.move(item, -x_move, 0)
            if coords[3] > canvas_height or coords[1] < 0:
                canvas.move(item, 0, -y_move)
        canvas.after(50, update_confetti, canvas, confetti, start_time)
    else:
        for item in confetti:
            canvas.delete(item)  # Remove confetti after animation

def startConfetti(canvas, on=True):
    if on:  # Start animation
        confetti = create_confetti(canvas)
        start_time = time.time()
        update_confetti(canvas, confetti, start_time)

class ClickTracker:
    def __init__(self, output_function, canvas):
        self.output_function = output_function
        self.canvas = canvas
        self.listener = mouse.Listener(on_click=self.on_click)
        self.tracking = False
        self.process_clicks = True  # New flag to control click processing
        self.click_count = 0

    def on_click(self, x, y, button, pressed):
        if self.process_clicks:
            if button == mouse.Button.left:
                if pressed:
                    self.start_time = time.time()
                else:
                    self.end_time = time.time()
                    duration = self.end_time - self.start_time
                    self.click_count += 1  # Increment click count
                    message = f"Click {self.click_count}: Duration: {duration:.3f} seconds.. Position: ({x}, {y})"
                    if self.click_count % 10 == 0:
                        message += f"\n❤️ -+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+~~~+-  ❤️"
                        startConfetti(self.canvas)
                    print("bezierMove(rnd.randint(",(x - 5),",",(x + 5),"), rnd.randint(",y-5,",",y+5,"), sleepy(.3))")
                    self.output_function(message)
            return

    def stop(self):
        self.process_clicks = False  # Stop processing clicks
                
    def run(self):
        try:
            self.tracking = True
            self.process_clicks = True
            with self.listener:
                #if not self.click_tracker_thread.is_alive():
                self.listener.join()
        except Exception as e:
            print(f"Error in ClickTracker: {e}")
        finally:
            self.tracking = False