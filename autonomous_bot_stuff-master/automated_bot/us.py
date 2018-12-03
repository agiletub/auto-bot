#Libraries
import RPi.GPIO as GPIO
import time
 
 
front_right=1
back_right=2
upper=3
front=4
back=5
left=6
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER= 16 
GPIO_ECHO = 20
 
#set GPIO direction (IN / OUT)
#for i in 5:
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def dist():
    GPIO.output(GPIO_TRIGGER , False)
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER ,True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
 
if __name__ == '__main__':
    try:
        while True:
            distance = dist()
            print ("Measured Distance = % .1f cm" %distance)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()