import RPi.GPIO as GPIO
from time import sleep  
GPIO.setmode(GPIO.BCM) 

GPIO.setup(17, GPIO.OUT)# set GPIO 17 as output for white led  
GPIO.setup(27, GPIO.OUT)# set GPIO 27 as output for red led  
GPIO.setup(22, GPIO.OUT)# set GPIO 22 as output for red led
blue = GPIO.PWM(17, 75)
green = GPIO.PWM(27, 75)
red = GPIO.PWM(22, 75)   



i = 25
try:
    while(True): 
        red.start(i*2)
        blue.start(i*2)
        sleep(0.5)
        red.stop()
        sleep(0.5)

        blue.start(i)
        green.start(i)
        sleep(0.5)
        blue.stop()
        sleep(0.5)
except KeyboardInterrupt:
        green.start(i)
        sleep(0.5)
        green.stop()
        sleep(0.5)
        GPIO.cleanup() 
        print("應用程式結束")