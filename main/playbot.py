import os
import sys
# Get the absolute path to the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the project root to the Python path
sys.path.insert(0, project_root)

from utils.timmy import *
from utils.welcome import *

sleep()

print("Helloooo World")  
welcome()
