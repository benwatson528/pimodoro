import blinkt
from RGB import RGB

WHITE_COLOUR = RGB(255, 255, 255)
NUM_PIXELS = blinkt.NUM_PIXELS

def updateProgressBar(timeRemaining, totalTimeSecs, barColour):
    for pixel in range(NUM_PIXELS):
            if (pixel/NUM_PIXELS < timeRemaining/totalTimeSecs):
                blinkt.set_pixel(pixel, barColour.r, barColour.g, barColour.b)
            else:
                blinkt.set_pixel(pixel, WHITE_COLOUR.r, WHITE_COLOUR.g, WHITE_COLOUR.b)
    blinkt.show()

def pulse(colour, frequency):
    brightness = 0.0
    stepSleep = frequency/10
    for i in range(10):
        blinkt.set_all(colour.r, colour.g, colour.b, brightness)
        brightness = brightness + stepSleep
        blinkt.show()

    for i in range(10):
        blinkt.set_all(colour.r, colour.g, colour.b, brightness)
        brightness = brightness - stepSleep
        blinkt.show()
