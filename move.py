#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from gazebo_msgs.srv import GetModelState

def _get_coords(name):
    model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    resp_coordinates = model_coordinates(str(name), 'world')
    return resp_coordinates.pose.position

def rotate(degrees, direction='left'):

    angular_speed = 0.8
    duration = abs(degrees) / 90.0 * 2.0 

    if direction == 'right':
        angular_speed = -angular_speed

    start_time = rospy.Time.now().to_sec()
    while rospy.Time.now().to_sec() - start_time < duration:
        cmd.angular.z = angular_speed
        pub.publish(cmd)
        rate.sleep()

    cmd.angular.z = 0
    pub.publish(cmd)

pos = _get_coords('rosbots')

print("Начальные координаты робота: ", pos.x, pos.y)

print('Введите через пробел координаты точки назначения в порядке: x, y')
coords = list(map(float, input().split()))
print(*coords)

rospy.init_node('command_node', anonymous=True)
pub = rospy.Publisher('/part2_cmr/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(100) # 10hz


cmd = Twist()
rate.sleep()
pos = _get_coords('rosbots')
flag = 0


if pos.x > coords[0]:
    flag = 1
    rotate(162,'left')
    cmd.linear.x = 1
    pub.publish(cmd)
    rate.sleep()

    while pos.x > coords[0]:
        pub.publish(cmd)
        rate.sleep()
        pos = _get_coords('rosbots')
else:
    cmd.angular.z = 0
    pub.publish(cmd)
    rate.sleep()
    cmd.linear.x = 1
    pub.publish(cmd)
    rate.sleep()
    while pos.x < coords[0]:
        pub.publish(cmd)
        rate.sleep()
        pos = _get_coords('rosbots')


if pos.y > coords[1]:
    if flag == 1:
        rotate(90, 'left')
    else:
        rotate(90, 'right')
    cmd.linear.x = 1
    pub.publish(cmd)
    rate.sleep()
    pos = _get_coords('rosbots')
    while pos.y > coords[1]:
        pub.publish(cmd)
        rate.sleep()
        pos = _get_coords('rosbots')
else:
    if flag == 1:
        rotate(90, 'right')
    else:
        rotate(90, 'left')
    cmd.linear.x = 1
    pub.publish(cmd)
    rate.sleep()
    pos = _get_coords('rosbots')
    while pos.y < coords[1]:
        pub.publish(cmd)
        rate.sleep()
        pos = _get_coords('rosbots')


cmd.linear.x = 0
pub.publish(cmd)
rate.sleep()

pos = _get_coords('rosbots')
print("Конечные координаты робота: ", pos.x, pos.y)
