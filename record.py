# importing the required packages
import pyautogui
import cv2
import numpy as np
from colorama import Fore, Back, Style
import keyboard

print(Fore.YELLOW + "This screen recorder made by Sajad pp ['https://github.com/mrsajadpp']!")
# display screen resolution, get it using pyautogui itself
SCREEN_SIZE = tuple(pyautogui.size())
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# frames per second
fps = 30.0
# file name
filename = input("File name: ")
# create the video write object
out = cv2.VideoWriter(filename + ".mp4", fourcc, fps, (SCREEN_SIZE))
# the time you want to record in seconds
value = True
# guide user
print(Fore.GREEN + "Recording started")
print(Fore.GREEN + "Saving 'Desktop/" + filename + ".mp4")
print(Fore.RED + "Stop recording CTRL+C")

while (value):
    # make a screenshot
    img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
