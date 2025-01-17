from pynput import keyboard
from pynput.keyboard import Listener

def on_press(key):
    print("Key pressed")
    

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()