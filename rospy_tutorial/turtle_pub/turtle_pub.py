#!/usr/bin/env python

from turtle import pu
import rospy
from geometry_msgs.msg import Twist

def main():

    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)


    pub_obj = Twist()

    while(not rospy.is_shutdown()):

        pub_obj.linear.x = 1.0
        pub_obj.angular.z = 0.2

        pub.publish(pub_obj)






if __name__ == '__main__':
    rospy.init_node('turtle_sim')
    main()
    