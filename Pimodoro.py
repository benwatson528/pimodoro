import colorsys
import time
import blinkt
from flask import Flask, render_template
from RGB import RGB
from LightFunctions import pulse, updateProgressBar

DEFAULT_BRIGHTNESS = 0.1

def runTimer(totalTimeMins, barColour):
    totalTimeSecs = totalTimeMins * 60
    timeRemaining = totalTimeSecs
    startTime = int(time.time())

    while timeRemaining > 10:
        print(timeRemaining)
        elapsedSecs = int(time.time()) - startTime
        timeRemaining = totalTimeSecs - elapsedSecs
        updateProgressBar(timeRemaining, totalTimeSecs, barColour)
        time.sleep(1)

    while timeRemaining > 0:
        elapsedSecs = int(time.time()) - startTime
        timeRemaining = totalTimeSecs - elapsedSecs
        pulse(barColour, 0.4)

def clearDisplay():
    blinkt.clear()
    blinkt.show()
