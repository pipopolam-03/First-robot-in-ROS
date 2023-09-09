import rospy
import time
from std_msgs.msg import String

rospy.init_node("messages")

robots = ["0", "1", "2"] 
count = [1, 1, 1] 
start_time = time.time()

I0 = [0, 0]
n0 = [0, 0]

I1 = [0, 0]
n1 = [0, 0]

I2 = [0, 0]
n2 = [0, 0]

R0 = [0, 0]
R1 = [0, 0]
R2 = [0, 0]

R_res_0 = [0, 0]
R_res_1 = [0, 0]
R_res_2 = [0, 0]

def message_callback(data, robot_id):
    message = data.data
    global count
    
    global message_0
    global message_1
    global message_2
    
    global I0
    global I1
    global I2
    
    global n0
    global n1
    global n2
    
    global R0
    global R1
    global R2
    
    global R_res_0
    global R_res_1
    global R_res_2

    if robot_id == "0":
        message_0 = message
        count[0] += 1
        if message_0 == message_1:
            n0[0] += 1
            
        if message_0 == message_2:
            #print('0: 2 is correct')
            n0[1] += 1
        
        I0[0] = n0[0] / count[1]
        
        if I0[0] > 0.5:
            R0[0] += I0[0]
        else:
            R0[0] += I0[0] -(R0[0] - 2.7**(-(1-I0[0])))
            
        I0[1] = n0[1] / count[2]
        
        if I0[1] > 0.5:
            R0[1] += I0[1]
        else:
            R0[1] += I0[1] -(R0[1] - 2.7**(-(1-I0[1])))
            
    elif robot_id == "1":
        message_1 = message
        count[1] += 1
        if message_1 == message_0:
            n1[0] += 1
            
        if message_1 == message_2:
            n1[1] += 1
        
        I1[0] = n1[0] / count[0]
        
        if I1[0] > 0.5:
            R1[0] += I1[0]
        else:
            R1[0] += I1[0] -(R1[0] - 2.7**(-(1-I1[0])))
            
        I1[1] = n1[1] / count[2]
        
        if I1[1] > 0.5:
            R1[1] += I1[1]
        else:
            R1[1] += I1[1] -(R1[1] - 2.7**(-(1-I1[1])))

    else:
        message_2 = message
        count[2] += 1
        if message_2 == message_0:
            n2[0] += 1
            
        if message_2 == message_1:
            n2[1] += 1
            
        I2[0] = n2[0] / count[0]
        
        if I2[0] > 0.5:
            R2[0] += I2[0]
        else:
            R2[0] += I2[0] -(R2[0] - 2.7**(-(1-I2[0])))
        
        I2[1] = n1[1] / count[1]
        
        if I2[1] > 0.5:
            R2[1] += I2[1]
        else:
            R2[1] += I2[1] -(R2[1] - 2.7**(-(1-I2[1])))
            
    
    E = time.time() - start_time
            
    R_res_0[0] = R0[0] / E
    R_res_0[1] = R0[1] / E
    
    R_res_1[0] = R1[0] / E
    R_res_1[1] = R1[1] / E
    
    R_res_2[0] = R2[0] / E
    R_res_2[1] = R2[1] / E
    
    print('Robot 0 reputation =', (R_res_1[0] + R_res_2[0])/2)
    print('Robot 1 reputation =', (R_res_0[0] + R_res_2[1])/2)
    print('Robot 2 reputation =', (R_res_0[1] + R_res_2[1])/2)

for robot in robots:
    rospy.Subscriber(f"/lidar_check_{robot}", String, message_callback, robot)

rospy.spin()
