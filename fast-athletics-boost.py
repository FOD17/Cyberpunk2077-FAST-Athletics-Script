import mouse
import time
import keyboard

# Give a kick off time
time.sleep(5)

# Kick off beserk and give slight pause before next stage
keyboard.press("e")
time.sleep(3)
keyboard.press("e")
time.sleep(3)
print("Beserk Ran")

# Throw Punch - make sure punch is selected
mouse.click("left")
time.sleep(0.25)
print("Punch Ran")

# Go into the menu
keyboard.press("m")
keyboard.release("m")
print('Menu Ran')
