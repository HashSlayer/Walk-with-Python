## Old-School-Walk-Scape #Created by @MekailTheMachine
OSWS; OSRS scripting bot for various skills. Created to improve GUI automation, and was made for educational purposes only.

Welcome to Mekail The Machine's basic OSRS skilling script using 100% python.

The script does not use object detection, and is recommend to run over RuneLite client. It was optimized to run on a screen
with 1920 x 1200 resolution, but works as well on 1920 x 1080 resolution.
The script was originally ran on an Ubuntu Linux machine, and later built for Windows, but may still work on Linux OS.

The script optimizes the use of the random module, often imported as "rnd" for abbreviation, integrated into functions
pulled from PyAutoGui, and Pythons Mouse library, to create random parameters between each click, and movement speeds.

PyAutoGui.MoveRel was implemented within movements to specific pixel locations. By calling the function, and prompting the machine to
move the cursor relative to it's current location, just prior to prompting it to move to a specific pixel location (as long as the time it takes to
move the cursor to the location is less than the time taken to move the cursor relatively, it will always end up on the desired location) 
this allowed for the cursor to pull itself into an alternate direction while moving, to allow for multiple line segmants in the movements.

Variables to account for sleep time were avoided, and manually coded in to ensure a new calculated  value was generated each time.

In darts.py the script is designed to click between the 15th and 16th item in the inventory slot; and is only programmed to take
short breaks between extensive clicks. It is designed to click different locations in random time parameters; moving in a diagonal fashion
with varying slopes and speeds to help reduce any bot detenction. More measures could certainly be implemented, but this was not made
for the inteded use of bot farming. This script was ran over a period of 2 weeks, for a couple hours a day, on a fresh account to 99.
The script runs at a pretty sweet pace, with realistic break points, but shouldn't be run for over 2 hours.

Firegod.py requires the user to click on the compass on the upper right of the screen to affix their screen's view to true north.
Then adjust the camera directly upwards, pointing further downwards in a bird eye fashion, then on the Eastern side of the Grand Exchange
on the row of tiles where the first bank teller is on the East side of the GE, you may walk 20 tiles out and begin the script with a tinder box
already in your inventory, and logs at the top right of your bank. It will grab the logs, walk back out, and burn them, but is optimzied to burn
logs that you are able to burn in 1 tick. The timing  currently isn't optimzed well, but can work well after small tweaks on the timining between lights.
^
this program iterates through the inventory by clicking on the first item, and reverting back 4 columns and down 1 row, every four items, until 
all spots have been clicked. This can be repurposed for many other skills. 
- the program then iterates between Eastern and Western columns to prevent from trying to burn logs on the some tiles as the previous iteration.

Fletcher.py fletches; was also made from the wineking code, and on a whim. in a couple minutes.

PixelHunter.py was used to grab spots of multiple pixel locations by hovering over the spot. The program could be 
repurposed to grab locations dependent on a button click if desired, but that makes it less fun.

potionmaker.py will help you make potions, many of the comments may have been copied and pasted from other files in this folder
and likely not fixed

WineKing.py is the original script made to make wine, and it does so at a fantastic rate, with random movements, breaks, and is timed to perfection.
To run this script, like many, make sure you set the item quantity ( X value ) of the items to take, to be x14. and your camera facing flat,
directly at a bank teller,  with the camera zoomed in. 
