from pyautogui import *
import pyautogui
import pydirectinput
import time
import keyboard
import random
import win32api, win32con
import subprocess
import smtplib
from dotenv import load_dotenv
import os



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click_rand_duration(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(random.uniform(0.05,0.1))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def generateIntArea(left_x, left_y, right_x, right_y, y_offset):
    # Calculate the slope of the line
    slope = (right_y - left_y) / (right_x - left_x)
    intercept = left_y - slope * left_x

    # Generate a random x within the bounds of the line segment
    random_x = random.randint(left_x, right_x)

    # Calculate the corresponding y on the line using the equation y = mx + b
    y_on_line = slope * random_x + intercept

    # Add a random offset to the y-coordinate within ±y_offset
    random_y = y_on_line + random.randint(y_offset, 0)

    # Return the random point
    return int(random_x), int(random_y)

def openClash():
    count = 0
    while pyautogui.pixel(1053, 443)[1] != 49:
        time.sleep(0.1)
        if count <= 50:
            break
    click(1114, 461)
    while pyautogui.pixel(445, 636)[1] != 226:
        time.sleep(0.1)
    click(445, 636)
    print("Opening clash")
    
def waitForOpen():
    while pyautogui.pixel(1232, 556)[0] != 0:
        time.sleep(0.1)
    while pyautogui.pixel(1060, 1060)[0] == 72: # Keep trying to fullscreen until it works
        time.sleep(0.1)
        pydirectinput.press("f11")
    print("The game is fullscreened")
    while pyautogui.pixel(1016, 83)[0] != 199:
        time.sleep(0.1)
    print("The game is open")

def closeClash():
    print("Closing Game")
    pydirectinput.keyDown('shift')
    pydirectinput.keyDown('tab')
    pydirectinput.keyUp('shift')
    pydirectinput.keyUp('tab')
    while pyautogui.pixel(1018, 330)[0] != 255:
        time.sleep(0.1)
    click(1018, 330)
    while pyautogui.pixel(1093, 599)[1] != 254:
        time.sleep(0.1)
    click(1093, 599)

def collectElixrCart():
    print("Moving to Elixr")
    time.sleep(random.uniform(0.2,0.5))
    pydirectinput.mouseDown(random.randint(958, 962), random.randint(538, 542))
    pydirectinput.moveTo(random.randint(955, 965), random.randint(595, 600), duration=time.sleep(random.uniform(0.2,0.5)))
    pydirectinput.mouseUp()
    time.sleep(random.uniform(0.2,0.5))
    print("Collecting Elixr")
    click_rand_duration(random.randint(1266, 1326), random.randint(1, 18)) # Open elixr car without moving
    time.sleep(random.uniform(0.2,0.5)) # Wait random time
    click_rand_duration(random.randint(1290, 1530), random.randint(880, 936)) # Press collect button
    time.sleep(random.uniform(0.2,0.5)) # Wait random time
    click_rand_duration(random.randint(1575, 1636), random.randint(87, 124)) # Press x button

def beginAndFindAttack():
    print("Starting attack")
    time.sleep(random.uniform(0.2,0.5)) # Wait random time
    click_rand_duration(random.randint(29, 178), random.randint(911, 1038)) # Press attack
    time.sleep(random.uniform(0.2,0.5))
    click_rand_duration(random.randint(1240, 1607), random.randint(659, 748)) # Press find now
    while pyautogui.pixel(996, 959)[2] != 254:
        time.sleep(0.1)
    print("Attack has started")

def placeTroops():
    pydirectinput.press('1')
    while pyautogui.pixel(996, 959)[2] == 254:  # 1048, 992 or no hero is 996, 959
        for i in range(2):
            x,y = generateIntArea(left_x=194, left_y=446, right_x=715, right_y=36, y_offset=-30)
            click_rand_duration(x, y)
            time.sleep(random.uniform(0.2,0.5))
        for i in range(2):
            x,y = generateIntArea(left_x=1255, left_y=43, right_x=1677, right_y=357, y_offset=-30)
            click_rand_duration(x, y)
            time.sleep(random.uniform(0.2,0.5))
        for i in range(2):
            x,y = generateIntArea(left_x=1411, left_y=895, right_x=1740, right_y=632, y_offset=-30)
            click_rand_duration(x, y)
            time.sleep(random.uniform(0.2,0.5))
    pydirectinput.press('q')
    for i in range(2):
        x,y = generateIntArea(left_x=194, left_y=446, right_x=715, right_y=36, y_offset=-30)
        click_rand_duration(x, y)
        time.sleep(random.uniform(0.2,0.5))
    for i in range(2):
        x,y = generateIntArea(left_x=1255, left_y=43, right_x=1677, right_y=357, y_offset=-30)
        click_rand_duration(x, y)
        time.sleep(random.uniform(0.2,0.5))
    for i in range(2):
        x,y = generateIntArea(left_x=1411, left_y=895, right_x=1740, right_y=632, y_offset=-30)
        click_rand_duration(x, y)
        time.sleep(random.uniform(0.2,0.5))

def automateAttacks():
    openClash()
    waitForOpen()
    collectElixrCart()
    beginAndFindAttack()
    placeTroops()
    closeClash()

import os
import smtplib

def main():
    load_dotenv()

    # Get information from env file
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('EMAIL_PASSWORD')
    recipient_email = os.getenv('RECIPIENT_EMAIL')

    try:
        for i in range(0):
            print(f"Starting attack {i+1}...")
            automateAttacks()

        # Connect to the notification email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the message
        server.sendmail(sender_email, recipient_email, "The clash attacks script is finished running.")

    except Exception as e:
        print(f"An error occurred: {e}")

        # Connect to the notification email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the message
        server.sendmail(sender_email, recipient_email, "There was an error running the clash script.")

    server.quit()

if __name__ == "__main__":
    main()
