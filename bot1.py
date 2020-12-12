import pyautogui
import time
import random

time.sleep(5)

file = open("test.txt", "r").read()
file = file.splitlines()

while True:
    pyautogui.typewrite(random.choice(file))
    pyautogui.press("enter")
    time.sleep(0.2)




