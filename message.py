import pyautogui
import time
time.sleep(6)
count=0
while count<=10:
    pyautogui.typewrite("aur lode kya kar raha hai! "+str(count))
    pyautogui.press("enter")
    count = count+1