import RPi.GPIO as GPIO
from time import sleep
import rgbLed 

if __name__ == '__main__':
    rgb = rgbLed.RGBLed(22,27,17)    
    rgb.redLight(forever = True)
    rgb.clean()
