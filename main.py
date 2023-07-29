from kfc import unicode_to_limon
import keyboard
import time
import pyperclip


# Define the time window (in seconds) within which the second "Ctrl+C" press is considered quickly repeated
QUICK_PRESS_WINDOW = 0.5

last_ctrl_c_time = 0

def on_key_event(event):
    global last_ctrl_c_time

    if event.name == 'c' and event.event_type == keyboard.KEY_DOWN and keyboard.is_pressed('ctrl'):
        current_time = time.time()
        if current_time - last_ctrl_c_time <= QUICK_PRESS_WINDOW:
            print("Quickly pressed Ctrl+C twice!")
            clipboard_content = pyperclip.paste()
            
            print("Clipboard content:")
            print(clipboard_content)

            unicode = clipboard_content
            limon = unicode_to_limon(unicode)
            print(f"unicode: {unicode} -> limon: {limon}")
            pyperclip.copy(limon)
            # Add your code here to do something when "Ctrl+C" is quickly pressed twice
        last_ctrl_c_time = current_time

keyboard.on_press(on_key_event)

print("Listening for Ctrl+C...")
keyboard.wait('esc')  # Wait until the 'Esc' key is pressed to exit the program






