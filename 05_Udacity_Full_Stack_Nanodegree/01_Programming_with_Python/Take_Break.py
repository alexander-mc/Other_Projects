# Project name: Take Break
# Project description: This brief program opens the webbrowser to a youtube video every x seconds. The intent is to remind the user to take a break after a certain amount of time.
# Course: Udacity Full Stack Nanodegree

# -----------------------------------

import webbrowser
import time

sleep_seconds = 10
count_breaks = 0

print("This program started on "+ time.ctime())

while (count_breaks < 3):
    time.sleep(sleep_seconds)
    webbrowser.open("https://www.youtube.com/watch?v=sl9voSKJmEU")
    count_breaks += 1
