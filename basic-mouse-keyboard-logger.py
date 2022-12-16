import pyautogui
import keyboard

def record_activity():
    print("Recording started. Press 'stop' to end recording.")
    mouse_clicks = []
    mouse_movements = []
    keyboard_strokes = []

    while True:
        mouse_position = pyautogui.position()
        mouse_movements.append(mouse_position)

        if pyautogui.click():
            mouse_clicks.append(mouse_position)

        if keyboard.read_key():
            key = keyboard.read_key()
            keyboard_strokes.append(key)
        
        if keyboard.is_pressed('stop'):
            break
    
    with open("activity_log.txt", "w") as output_file:
        output_file.write("Mouse Movements\n")
        for movement in mouse_movements:
            output_file.write(str(movement) + "\n")
        output_file.write("\nMouse Clicks\n")
        for click in mouse_clicks:
            output_file.write(str(click) + "\n")
        output_file.write("\nKeyboard Strokes\n")
        for stroke in keyboard_strokes:
            output_file.write(str(stroke) + "\n")
    
    print("Recording stopped. Results written to activity_log.txt")

if keyboard.is_pressed('start'):
    record_activity()
else:
    print("Press 'start' to begin recording.")
