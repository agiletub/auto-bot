import RPi.GPIO as GPIO
from time import sleep
import math

GPIO.setmode(GPIO.BCM)

pina=17
#a is the one which moves the right motor forward no
pinb=27
#b is the one which moves the right motor backward no
pinc=23
#c is the one which moves the left motor forward no
pind=24
#d is the one which moves the left motor backward no
l293d_pin=4

GPIO.setup(17,GPIO.OUT)
GPIO.setup(pinb,GPIO.OUT)
GPIO.setup(pinc,GPIO.OUT)
GPIO.setup(pind,GPIO.OUT)

a=GPIO.PWM(pina,100)
a.start(0)

b=GPIO.PWM(pinb,100)
b.start(0)

c=GPIO.PWM(pinc,100)
c.start(0)

d=GPIO.PWM(pind,100)
d.start(0)

GPIO.setup(l293d_pin,GPIO.OUT) 
GPIO.output(l293d_pin, True)


max_motor_speed=100
default_motor_speed=max_motor_speed/2


def set_speed(motor_name, speed):
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(0)
    c.ChangeDutyCycle(0)
    d.ChangeDutyCycle(0)
    
    value= abs(speed)
    
    
    if motor_name[0]=='r':   #add lower again
             if speed >0:
                 GPIO.output(pina, True)
                 b.ChangeDutyCycle(value)
             if speed<0:
                 GPIO.output(pinb, True)
                 a.ChangeDutyCycle(value)
                 
    if motor_name[0]=='l':   #add lower again
             if speed>0:
                 GPIO.output(pinc, True)
                 d.ChangeDutyCycle(value)
             if speed<0:
                 GPIO.output(pind, True)
                 c.ChangeDutyCycle(value)
             
   