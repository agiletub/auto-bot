import distances
import us
import motion
import vision


#have to define time properly

path=[]
box_coordinates=[]
qr_coordinates=[]
start_coordinates=[]
end_coordinates=[]
time0=time.time()

##################################################################################
#waits until block cleared
def wait_for_path():
	while distances.front_blocked and distances.check_for_qr():
		pass
	
	motion.forward()
	path.append(['forward',time])

##################################################################################
def path_trim(path,start,end):
    length=len(path)-1
    while True:
        if i==1:
            break
        if path[i-1,i+1]==['left','left']:
            tail=path[i+1:]
            head=path[0:i]
            path= head.extend(tail)
        i-=1
##################################################################################
def min_path(path1,path2):        
    
##################################################################################
def move():

	#measure time elapsed
        time=time.time()-time0
	#right check
	if distances.box_on_right:
		motion.turn('right')
		path.append(['right',time])

	elif distances.right_open:
		motion.turn(right)
		path.append(['left',time])
		motion.forward()
		path.append['forward',time]

	#front check
	elif distances.front_blocked:

		if vision.check_for_box():
			motion.stop()
			
			#stores box coordinate in path
			box_coordinates.append(len(path)-1)
			
			
			wait_for_path()

		elif distances.check_for_qr():
			motion.stop()
			qr_coordinates.append(len(path)-1)
			number_of_boxes_found=len(box_coordinates)

			if number_of_boxes_found<2:
				motion.turn('left')
			else: wait_for_path()	

		else:
			motion.turn('left')
			path.append(['left',time])

	#define start-end coordinates
	if vision.ground_is_white:
		if len(start_coordinates)<2:
			start_coordinates.append(len(path)-1)
		else: 
			end_coordinates.append(len(path)-1)
		if len(start_coordinates)==2:
			path.clear()
			follow_path=min_path(path_trim(path,start[0],qr_coordinates[0]),path_trim(start[1],qr_coordinates[0]))
			time=0
			

	#call method again
	move()		
##################################################################################

'''methods used 

motion.forward()             partially done
motion.turn(direction)
motion.stop()
vision.check_for_block()
distances.check_for_qr()
follow_path(path)
path.clear()
min_path(path1,path2)
'''


'''variables used

vision.groundiswhite      
distances.box_on_right    done
distances.right_open      done
distances.front_block     done
path[[direction,time]]

'''
