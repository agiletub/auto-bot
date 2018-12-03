import us
import feedback_loop
import time
import motion


front_blocked=False
box_on_right=False
right_open=False

def check_for_qr():
    #checks if a qr bock is present whithin 35 cm of stand
    if dist(upper)<35:
        #goes to the required range kept 1 cm extra as error due to no brakes.
        if dist.upper>=26:
            motion.forward()
            check_for_qr()
        elif dist.upper<=24:
            motion.backward()
        #stops if already in range 
        else:
            motion.stop()
        return True
#following two lines are carried out at the start of the run
last_value=[us.dist(us.right_front),us.dist(us.right_back)]
second_last_value=[us.dist(us.right_front),us.dist(us.right_back)]

while True:
    
    right_uss_values=[us.dist(us.right_front),us.dist(us.right_back)]
    
    
    # check if current= open, close and 2nd last value=close,open
    if right_uss_values[0]<10 and right_uss_values[1]>10 :
        if second_last_value[0]>10 and second_last_value[1]<10:
            box_on_right=True
           #removes the case where the bot may get confused after passing the qr block
            #last_value=[0,0]
            #second_last_value=[0,0]
            
            
            
    #checks if current= open, open
    elif right_uss_values[0]>10 and right_uss_values[1]>10:
        right_open=True
    #if neither, both are false
    else:
        right_open= False
        box_on_right=False
        
        
    #stores last 2 values everytime the current value changes
    if not last_value==right_uss_values:
        second_last_value=last_value
        last_value=right_uss_values
        
        
    
    #checks if bot can go forward or not error due tobreaks ideal=5
    if us.dist(us.front)<=7:
        front_blocked=True
        
        
        
    #takes reading every 10 milliseconds
    time.sleep(0.01)
    
    
'''
make a method in us to calc dist every shortest delay for all sensor and make others access from it by importing it
'''

    
    
    