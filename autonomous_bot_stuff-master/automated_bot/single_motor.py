
import cv2
import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)

l293d_pin=10
Motor3 = 24

GPIO.setup(Motor3,GPIO.OUT)
GPIO.setup(l293d_pin,GPIO.OUT) 


GPIO.output(Motor3,False)
GPIO.output(l293d_pin,False)



GPIO.output(l293d_pin, True)

 
GPIO.output(Motor3,True)
