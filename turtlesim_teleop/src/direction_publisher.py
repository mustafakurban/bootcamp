#! /usr/bin/env python3

import termios
import tty
import sys
import rospy
import select
from std_msgs.msg import String

class keyListener:
    def __init__(self):
        self.key_timeout = 0.05
        self.settings = termios.tcgetattr(sys.stdin)
    def getKey(self):
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], self.key_timeout)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key

rospy.init_node("direction_publisher_python")
pub = rospy.Publisher("direction", String, queue_size=1)
rate = rospy.Rate(10)
msg = String()
listener = keyListener()
while not rospy.is_shutdown():
    if listener.getKey() == "w":
        msg.data = "forward"
    elif listener.getKey() == "s":
        msg.data = "backward"
    elif listener.getKey() == "a":
        msg.data = "left"
    elif listener.getKey() == "d":
        msg.data = "right"
    elif listener.getKey() == "q":
        for i in range(10):
            msg.data = "EXITING"
            pub.publish(msg)
        break
    else:
        msg.data = "stop"
    pub.publish(msg)