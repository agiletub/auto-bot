import time
import motor
import distances
import us
import feedback_loop


go_forward=True
def forward():
    integral_error=0
    last_error=feedback_loop.ideal_right_wall_dist-us.dist()
    while go_forward==True:
        values=feedback_loop.adjustment_values(us.dist(),integral_error,last_error)
        pid_value= values[0]/100
        integral_error=values[1]
        last_error=values[2]
        print(pid_value)
        motor.set_speed('right',motor.default_motor_speed-pid_value)
        motor.set_speed('left',motor.default_motor_speed+pid_value)
        time.sleep(0.150)

def stop():
    go_forward=False
    motor.set_speed('right',0)
    motor.set_speed('left',0)
    

def turn(direction):
    pass




forward()