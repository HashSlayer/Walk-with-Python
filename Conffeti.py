import random
import time
import tkinter as tk

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
