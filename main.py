import os
import string
import random
import pyautogui
import time

chars = string.ascii_letters + string.digits + '!@#$%^&*()'  # List of all used text characters (Can be changed).


target_x, target_y = (800,810) # Screen coordinates to move mouse to.
delay = 15 # Delay in seconds between each message.

def text(amount):  # Function to randomly generate a string of text.
    random.seed = (os.urandom(1024))  # Random seed for generating text.
    return "".join(random.choice(chars) for i in range(amount))  # Returns randomized string of text as a variable.

time.sleep(3)  # Waits 3 seconds.

while True:  # This loop will never end unless the program is closed.
    pyautogui.moveTo(target_x, target_y)  # Moves mouse cursor to discord text box (My screen res is 1600x900)

    pyautogui.typewrite(text(15)) # Types random string of text.
    pyautogui.hotkey("enter") # 'Presses' enter key.

    time.sleep(delay)  # Waits a desired amount of time based on the 'delay' variable.
