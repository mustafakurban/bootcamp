#!/usr/bin/env python

import rospy
from rospy_tutorial.msg import example

def talker():
    pub = rospy.Publisher('custom_chatter', example, queue_size=10)
    rospy.init_node('custom_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        ex_pbj = example()
        ex_pbj.first_name = "mustafa"
        ex_pbj.last_name  = "kurban"

        rospy.loginfo(ex_pbj)
        pub.publish(ex_pbj)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass