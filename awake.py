import pyautogui
import time

def on_mouse_move(x, y):
    print(f"Mouse moved to ({x}, {y}).")

def main():
    initialMousePos = pyautogui.position()
    startTime = time.time()
    timeComparison = 240


    while True:
        currentMousePos = pyautogui.position()
        if currentMousePos != initialMousePos:
            on_mouse_move(*currentMousePos)
            initialMousePos = currentMousePos
            startTime = time.time()
        elif int(time.time() - startTime) == timeComparison:
             pyautogui.moveTo(200, 200, duration=0.10)
             pyautogui.moveTo(200, 800, duration=0.10)
             pyautogui.moveTo(1275, 800, duration=0.10)
             pyautogui.moveTo(1275, 200, duration=0.10)
             pyautogui.moveTo(200, 200, duration=0.10)
             pyautogui.keyDown('shift')
             pyautogui.keyUp('shift')
             initialMousePos = pyautogui.position()
             startTime = time.time()


   


main()