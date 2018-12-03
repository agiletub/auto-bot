import feedback_loop
import time
import math

def method1():
	angle=0
	disp=0
	right_wall_distance=0.08
	last_error=0
	integral_error=0
	delay=0.01
	while True:
		values= feedback_loop.adjustment_values(right_wall_distance,integral_error,last_error)
		pid_value=values[0]
		#print 'pid_value='+ str(pid_value)
		integral_error=values[1]
		last_error=values[2]
		angle=(pid_value*delay)/0.1
		print 'angle='+str(math.degrees(angle))
		disp=pid_value*delay
		time.sleep(0.1)
		right_wall_distance+=math.sin(angle)*disp
		print 'dist='+str(right_wall_distance*100)

def method2():

	disp=0
	dist1=10
	dist2=15
	last_error=5/15
	integral_error=0
	delay=0.01
	while True:
		values= feedback_loop.other_idea(dist1,dist2,integral_error,last_error)
		pid_value=values[0]
		print 'pid_value='+ str(pid_value)
		integral_error=values[1]
		last_error=values[2]
		disp=pid_value*delay
		time.sleep(0.1)


		dist1+=disp*1.25*math.sin(last_error)
		dist2-=disp*1.25*math.sin(last_error)
		print 'angle='+str(last_error)
		print 'dist1='+str(dist1)
		print 'dist2='+str(dist2)

#method1()
method2()