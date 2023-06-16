from gpiozero import Button
from signal import pause
from random import randint

button = Button(18)
def user_press():
    r = randint(0,100)/100;
    g = randint(0,100)/100;
    b = randint(0,100)/100;
    print("R={},G={},B={}".format(r,g,b));
    led.color = (r,g,b);

button.when_pressed = user_press;
pause()