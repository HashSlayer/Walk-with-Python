import time
import pyautogui as pag
import random as rnd
import math
from .MainFunctions import *

def bezier_between(x1, x2, y1, y2, time = 1.1):
    bezierMoveSmooth(rnd.randint(x1, x2), rnd.randint(y1, y2), (rnd.random() * time/2) + (time - time/9)) # move mouse to banker.

def bezier_relative(x1, x2, y1, y2, time = 0.3):
    bezierMoveRelative(rnd.randint(x1, x2), rnd.randint(y1, y2), (rnd.random() * time/2) + (time - time/9)) # move mouse to banker.


def bezierMoveRelative(dx, dy, duration=0.23 + rnd.random() * 0.15):
    start_x, start_y = pag.position()
    end_x, end_y = start_x + dx, start_y + dy  # Calculate the absolute end position

    # Choose control points
    control_x = rnd.choice([start_x, end_x]) + rnd.randint(-100, 100)
    control_y = rnd.choice([start_y, end_y]) + rnd.randint(-100, 100)
    p0 = (start_x, start_y)
    p1 = (control_x, control_y)
    p2 = (end_x, end_y)

    steps = int(duration * rnd.randint(90, 190))
    for i in range(steps):
        t = i / float(steps)
        target_x, target_y = quadratic_bezier(p0, p1, p2, t)
        perturbation_x = rnd.randint(-1, 1)
        perturbation_y = rnd.randint(-1, 1)
        pag.moveTo(target_x + perturbation_x, target_y + perturbation_y, _pause=False)
        time.sleep(duration / steps * (0.1 + 0.2 * math.sin(math.pi * t / 2)))
        if rnd.random() < 0.03:
            time.sleep(rnd.uniform(0.03, 0.1))

    # Ensure final position is reached accurately
    pag.moveTo(end_x, end_y, _pause=False, duration=rnd.random() * 0.04 + 0.04)
    

#Moving into bezierMove we aim to use multiple bezier curves to move the mouse in a more human like fashion, with dynamic speed and acceleration.
def quadratic_bezier(p0, p1, p2, t):
    """Calculate the quadratic Bezier curve point at t."""
    x = ((1 - t) ** 2) * p0[0] + 2 * (1 - t) * t * p1[0] + (t ** 2) * p2[0]
    y = ((1 - t) ** 2) * p0[1] + 2 * (1 - t) * t * p1[1] + (t ** 2) * p2[1]
    return (x, y)


def bezierMove(x, y, speed_multiplier= 1 + rnd.random() * 0.01):
    start_x, start_y = pag.position()
    distance = math.hypot(x - start_x, y - start_y)

    # Dynamic duration based on distance and speed_multiplier
    duration = (max(0.1, 0.15 + rnd.random() * 0.1 * (distance / 130))) * speed_multiplier

    # Dynamically adjust control point variation based on distance
    control_variation = min(100, max(30, int(distance / 6)))

    # Initial delay
    time.sleep(rnd.uniform(0.05, 0.1))

    control_x = rnd.choice([start_x, x]) + rnd.randint(-control_variation, control_variation)
    control_y = rnd.choice([start_y, y]) + rnd.randint(-control_variation, control_variation)
    p0 = (start_x, start_y)
    p1 = (control_x, control_y)
    p2 = (x, y)

    steps = int(duration * 100)  # More steps for smoother movement
    for i in range(steps):
        t = i / float(steps)
        # Adaptive speed: start slow, speed up, then slow down
        adaptive_speed = duration / steps * (0.1 + 0.5 * math.sin(math.pi * t))
        target_x, target_y = quadratic_bezier(p0, p1, p2, t)
        perturbation_x = rnd.randint(-1, 1)
        perturbation_y = rnd.randint(-1, 1)
        pag.moveTo(target_x + perturbation_x, target_y + perturbation_y, _pause=False)
        time.sleep(adaptive_speed)
        if rnd.random() < 0.03:
            time.sleep(rnd.uniform(0.03, 0.1))

    # Slight inaccuracy at the end for realism
    pag.moveTo(x, y, _pause=False, duration=rnd.random() * 0.02 + 0.03)
        

def randomMove(duration=0.5):
    start_time = time.time()
    while time.time() - start_time < duration:
        # Random small movements
        dx, dy = rnd.randint(-1, 1), rnd.randint(-1, 1)
        pag.moveRel(dx, dy, duration=0.1)

        # Random short pauses
        time.sleep(rnd.uniform(0.05, 0.2))

#Define a function that makes random and realistic mouse movements totaling about 2 seconds. + or - 0.2 seconds.
def Notbotting():
    sleep(0.01, .01, .01) #sleep
    bezierMove(rnd.randint(69, 1400), rnd.randint(69,880), 0.43 + 0.2 * rnd.random())
    randomMove(0.01 + 0.1 * rnd.random())
    bezierMove(rnd.randint(69, 1400), rnd.randint(69,880), 0.33 + 0.2 * rnd.random())# random movement
    time.sleep(0.1 + 0.1 * rnd.random())

#Define another Notbotting function that makes random and realistic mouse movements totaling about 3 seconds. + or - 0.2 seconds, with a different range of movement.

def Notbotting2():
    #using bezierMove, sleep, and randomMove, kRadom we can create a more realistic randomized movement.
    sleep(0.01, .01, .01) #sleep
    bezierMove(rnd.randint(69, 1400), rnd.randint(69,880), 0.43 + 0.2 * rnd.random())
    randomMove(0.01 + 0.1 * rnd.random())
    if rnd.random() > 0.9:
        for _ in range(0, rnd.randint(2, 7)):
            kRandom()
    kRandom()
    bezierMove(rnd.randint(69, 1400), rnd.randint(69,880), 0.33 + 0.2 * rnd.random())# random movement
    time.sleep(0.1 + 0.1 * rnd.random())
    randomMove(0.1 + 0.1 * rnd.random())
    sleep(0.01, .01, .01) #sleep
    k1()
    if rnd.random() > 0.5:
        k1()
    bezierMove(rnd.randint(-70, 74), rnd.randint(-99,12), 0.43 + 0.01 * rnd.random() + 3/27 * rnd.random())
    bezierMove(rnd.randint(-40, 74), rnd.randint(-80,60), 0.33 + rnd.random() * 0.1) # random movement
    time.sleep(0.1 + 0.1 * rnd.random())



#Let's simplify the time.sleep function slightly since we will be using it extensively..
def sleep(c = .01 , x = .008, z = 0.008): #C is a constant. X and Z are both multiplied by a number between 0-1.
    time.sleep(c + rnd.random() *x + rnd.random() *z) #Set variables so sleep() is viable for a .01 ~ .05 second sleep

#Define a function for random sleep variance from .1-.5 seconds ~
def sleepif(x=0.01):
    if (rnd.random() > 0.103):
        time.sleep(rnd.random() *0.001 + 0.001)
        if (rnd.random() > 0.008284):
            time.sleep(rnd.random() *0.001 + 0.001)
            if (rnd.random() > 0.09420):
                time.sleep(rnd.random() * x + 0.005)
            if (rnd.random() > 0.263):
                time.sleep(rnd.random() * x + 0.01)
            if (rnd.random() > 0.381251):
                time.sleep(rnd.random() * (x * 2) + 0.01)
            if (rnd.random() > 0.591251):  
                time.sleep(rnd.random() * (x * 2) + 0.01)
            if (rnd.random() > 0.793):
                time.sleep(rnd.random() * (x * 3) + 0.02)
            if (rnd.random() > 0.891251):
                time.sleep(rnd.random() * (x * 4) + 0.02)
            if (rnd.random() > 0.9180251):  
                time.sleep(rnd.random() * (x * 28) + 0.02)
            if (rnd.random() > 0.981251):  
                time.sleep(rnd.random() * (x * 9) + 0.04)
                if (rnd.random() > 0.89):
                    time.sleep(rnd.random() *0.09 + 0.04) 
                    if (rnd.random() > 0.871251):
                        time.sleep(rnd.random() *0.05 + 0.05)
                        print(" Long click!")
    if (rnd.random() > 0.991251):  
        time.sleep(rnd.random() *0.003 + 0.001)

