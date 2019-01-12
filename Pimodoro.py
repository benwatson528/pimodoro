import colorsys
import time
import blinkt
from RGB import RGB

DEFAULT_BRIGHTNESS = 0.1
STUDY_TIME = 10
REST_TIME = 5
NUM_PIXELS = blinkt.NUM_PIXELS

blinkt.set_clear_on_exit()
blinkt.set_brightness(0.1)

def runTimer(totalTime, startColour, endColour):
    timeRemaining = totalTime
    while timeRemaining > 0:
        for pixel in range(NUM_PIXELS):
            if (pixel/NUM_PIXELS < timeRemaining/totalTime):
                blinkt.set_pixel(pixel, startColour.r, startColour.g, startColour.b)
            else:
                blinkt.set_pixel(pixel, endColour.r, endColour.g, endColour.b)
        blinkt.show()
        timeRemaining = timeRemaining - 1
        time.sleep(1)

runTimer(STUDY_TIME, RGB(255, 0, 0), RGB(255, 255, 255))
runTimer(REST_TIME, RGB(0, 255, 0), RGB(255, 255, 255))

blinkt.clear()
blinkt.show()