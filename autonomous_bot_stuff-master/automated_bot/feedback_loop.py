'''import distances
from motion import motor_speed'''
import math

ideal_right_wall_dist=5
ideal_left_wall_dist=5
delay=0.150
total_distance=10



def adjustment_values(right_wall_dist,integral_error,last_error):

		#defining distances
	#self.right_wall_dist=right_wall_dist
	#self.left_wall_distance=left_wall_distance



		#init errors 

	error= ideal_right_wall_dist-right_wall_dist
	integral_error+=error*delay
	diff_error=(error-last_error)/delay
	last_error=error

		#define tuning constants
	Kp= 0.5
	Ki=0.3
	Kd=0.3

	P=Kp*error
	I=Ki*integral_error
	D=Kd*diff_error
	print(P)
	print(I)
	print(D)
	if integral_error>=0.15 or integral_error<=-0.15:	integral_error=0
	pid_value=P+I+D

	return [pid_value,integral_error,last_error]

	'''set_motor_speed('right',motion.default_motor_speed-(P+I+D))
	set_motor_speed('left',motion.default_motor_speed+(P+I+D))
'''


'''
		5:3:3
		500:375:25
		'''

delay=0.01

length=15
def other_idea(dist1,dist2,integral_error,last_error):
	error=math.asin((dist1-dist2)/length) #gives angle of inclination
	integral_error+=error*delay
	diff_error=(error-last_error)/delay
	last_error=error

	Kp=0.5
	Ki=0.1
	Kd=0.5

	P=Kp*error
	I=Ki*integral_error
	D=Kd*diff_error
	print(P)
	print(I)
	print(D)

	pid_value=P+I+D

	return [pid_value,integral_error,last_error]







