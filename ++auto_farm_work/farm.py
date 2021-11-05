import pyautogui, time, keyboard

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

pyautogui.click(484, 1011)

while True:

    keyboard.write("c!work")
    pyautogui.press("enter")
    time.sleep(3.1)
