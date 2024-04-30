import pyautogui
import time
import random
import numpy as np



def on_mouse_move(x, y):
    #print(f"Mouse moved to ({x}, {y}).")
    pass

def bezier_curve(p0, p1, p2, p3, num_points=4):
    # Create an array of parameter values from 0 to 1
    t = np.linspace(0, 1, num_points)

    # Compute the x and y coordinates of the points along the curve
    x = ((1 - t) ** 3) * p0[0] + 3 * ((1 - t) ** 2) * t * p1[0] + 3 * (1 - t) * (t ** 2) * p2[0] + (t ** 3) * p3[0]
    y = ((1 - t) ** 3) * p0[1] + 3 * ((1 - t) ** 2) * t * p1[1] + 3 * (1 - t) * (t ** 2) * p2[1] + (t ** 3) * p3[1]

    # Return the x and y coordinates as a list of tuples
    return list(zip(x, y))


def main():
    initialMousePos = pyautogui.position()
    startTime = time.time()
    timeComparison = random.randint(0,240)
    keys = ['shift', 'up', 'down', 'left', 'right']
    moves = random.randint(1,4)

    # Define the control points of the Bézier curve
    p0 = (random.randint(0, 1919), random.randint(0, 1079))
    p1 = (random.randint(0, 1919), random.randint(0, 1079))
    p2 = (random.randint(0, 1919), random.randint(0, 1079))
    p3 = (random.randint(0, 1919), random.randint(0, 1079))

    # Compute points along the Bézier curve
    curve_points = bezier_curve(p0, p1, p2, p3)



    while True:
        currentMousePos = pyautogui.position()
        if currentMousePos != initialMousePos:
            #on_mouse_move(*currentMousePos)
            initialMousePos = currentMousePos
            startTime = time.time()
        elif int(time.time() - startTime) == timeComparison:
           
            for _ in range(moves):

                if random.random() < random.uniform(0.0, 0.5):
                    pyautogui.moveTo(random.randint(0, 1919), random.randint(0, 1079), duration=random.uniform(0.1, 0.75))
                    initialMousePos = currentMousePos

                    if currentMousePos != initialMousePos:
                        break

                else:

                    for point in curve_points:
                        pyautogui.moveTo(point[0], point[1], duration=random.uniform(0.1, 0.4))
                        initialMousePos = currentMousePos

                        if currentMousePos != initialMousePos:
                            break
                
            chosenKey = random.choice(keys)
            pyautogui.keyDown(chosenKey)
            pyautogui.keyUp(chosenKey)

            initialMousePos = pyautogui.position()
            startTime = time.time()

            timeComparison = random.randint(0,240)
            print(timeComparison)
            moves = random.randint(1,4)

            # Define the control points of the Bézier curve
            p0 = (random.randint(0, 1919), random.randint(0, 1079))
            p1 = (random.randint(0, 1919), random.randint(0, 1079))
            p2 = (random.randint(0, 1919), random.randint(0, 1079))
            p3 = (random.randint(0, 1919), random.randint(0, 1079))

            # Compute points along the Bézier curve
            curve_points = bezier_curve(p0, p1, p2, p3)
             


   


main()
