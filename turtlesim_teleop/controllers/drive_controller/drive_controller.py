#! /usr/bin/env python3

from controller import Robot,Lidar
import rospy
import time
from std_msgs.msg import Int64, String

def direction_callback(data):
    global direction
    direction = data.data

direction = "sdfs"
robot = Robot()
timestep = int(robot.getBasicTimeStep())

lidar = robot.getDevice("LDS-01")
Lidar.enable(lidar, timestep)
Lidar.enablePointCloud(lidar)

right_engine = robot.getDevice("right wheel motor")
left_engine = robot.getDevice("left wheel motor")
right_engine.setPosition(float('+inf'))
left_engine.setPosition(float('+inf'))

rospy.init_node("lidar_listener")
pub = rospy.Publisher("/lidar_data",Int64,queue_size=1)
sub = rospy.Subscriber("/direction",String,direction_callback)
publish_msg = Int64()
starting_time = time.time()
while True:
    # point_cloud = Lidar.getPointCloud(lidar)
    # publish_msg.data = len(point_cloud)
    # pub.publish(publish_msg)
    if direction == "forward":
        right_engine.setVelocity(6.5)
        left_engine.setVelocity(6.5)
    elif direction == "backward":
        right_engine.setVelocity(-6.5)
        left_engine.setVelocity(-6.5)
    elif direction == "left":
        right_engine.setVelocity(6.5)
        left_engine.setVelocity(2)
    elif direction == "right":
        right_engine.setVelocity(2)
        left_engine.setVelocity(6.5)
    elif direction == "stop":
        right_engine.setVelocity(0)
        left_engine.setVelocity(0)
    elif direction == "EXITING":
        break
    else:
        pass
    robot.step(timestep)

