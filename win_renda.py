import pyautogui
import time
import keyboard

print("Press Enter to start/stop spamming Enter key.")

running = False  # Flag to track whether spamming is active

while True:
    keyboard.wait("enter")  # Wait for Enter key to toggle state
    running = not running  # Toggle running state
    print("Spamming started" if running else "Spamming stopped")
    
    while running:
        if keyboard.is_pressed("esc"):  # Stop immediately if Esc is pressed
            print("\nStopping the key press.")
            running = False
            break

        pyautogui.keyDown("enter")  # Press and hold Enter
        time.sleep(0.05)  # Hold the key for 50ms
        pyautogui.keyUp("enter")  # Release Enter
        time.sleep(0.05)  # 50ms interval
