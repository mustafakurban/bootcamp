#!/usr/bin/env python
import rospy

import random
from std_msgs.msg import Int32

class Talker():
    def __init__(self):
        self.pub = rospy.Publisher('chatter', Int32,queue_size=10)
        self.rate = rospy.Rate(1) #hz

    def Talk(self):
        msg = Int32()
        while(not rospy.is_shutdown()):
            msg.data = random.randint(0,100)
            rospy.loginfo(msg)

            self.pub.publish(msg)
            self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node('talker', anonymous=True)
    talker = Talker()
    talker.Talk()