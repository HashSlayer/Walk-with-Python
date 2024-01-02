# Old-School-Walk-Scape 
## Created by @5MEkailO

OSWS; OSRS scripting bot for various skills. Created to improve GUI automation, made for educational purposes

Welcome to Mekail The Machine's basic OSRS skilling script using python.

It was optimized to run on a screen with 1920 x 1080 resolution, or has features to help adjust the coordinates manually.
The script is safe to use on Linux, MacOS, and Windows.

# Developer Setup <img height=20/>

1. Install Python 3.10 (not compatible with other major versions)
2. Clone/download this repository
3. Open the project folder in your IDE of choice (Visual Studio Code recommended)
4. install the depedencies pip install -r requirements.txt
5. Run the files locally, or from your terminal

## User Interface

OSWS uses Tkinter to display a GUI in many scripts to handle automation processes, and visual command logging to track progress, as well as confetti to celebrate events,

## Human-like Mouse Movement
OSWS uses altered Bezier curves to create smooth, human-like mouse movements; and random pauses, stops, and occasional mistakes with path correct. 

# Scripts

A2 Functions, and MainFunctions act as Utility files, containing definitions for various functions that automate the process of time.sleep(),
and obsfucate mouse.click with pag to click the left mouse button for a duration of .1 - .3 seconds etc..
Automation for pressing keys 1-9, recommended remapping of keys through runelite to match, and more.

BeautifulTest tracks the position of the mouse when clicked, celebrating every 10 clicks. Used to find pixel locations and replaced PixelHunter.

AutoClicker is an Auto Clicker with variables to define time between clicks, user controlled random variance, and maximum amount of clicks.

GUI3 is a template for implementing a new GUI; issues arise when importing classes and functions for reuse, as Tkinter is not exactly thread safe.

