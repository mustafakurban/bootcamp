#!/usr/bin/env python
import rospy
import sys
from std_msgs.msg import Int32

class Listener:

  def __init__(self):
    self.sub = rospy.Subscriber("chatter",Int32,self.callback)

  def callback(self,data):
    print(data.data)



def main(args):
  obc = Listener()
  rospy.init_node('simple_class', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':
    main(sys.argv)