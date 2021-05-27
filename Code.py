import keyboard
import mouse
import time
running=False
def toggle():
    global running
    running = not running
keyboard.add_hotkey('alt+1', toggle)
print("Press alt+1 to toggle and alt+q to close")
while True:
    if keyboard.is_pressed('alt+q'):
        quit()
    elif running==True:
        mouse.click("left")
