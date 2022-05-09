#!/usr/bin/env python3
import time
import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty, threading

class keyListener:
    def __init__(self):
        self.key_timeout = 1
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



class Teleop:

    def __init__(self):
        # driving parameters are initialized

        self.step = 0.2
        self.gear_angular = 0
        self.gear_linear = 0
        self.max_gear = 10

        # required classses
        self.key_listener = keyListener()
        self.twist = Twist()


        x = threading.Thread(target=self.key_threat_func)
        x.start()

        # This expresses velocity in free space broken into its linear and angular parts.
        # Vector3  linear
        # Vector3  angular

        # Compact Message Definition
        # geometry_msgs/Vector3 linear
        # geometry_msgs/Vector3 angular

        self.pub_twist = rospy.Publisher('/diff_drive_controller/cmd_vel', Twist, queue_size=10)

        self.main()

    def pubTwist(self):
        
        # if(self.linear_velocity > self.max_linear_velocity):
        #     self.linear_velocity = self.max_linear_velocity
        # elif(self.linear_velocity < - self.max_linear_velocity):
        #     self.linear_velocity = - self.max_linear_velocity

        # if(self.angular_velocity > self.max_angualar_velocity):
        #     self.angular_velocity = self.max_angualar_velocity
        # elif(self.angular_velocity < - self.max_angualar_velocity):
        #     self.angular_velocity = -self.max_angualar_velocity

        if(self.gear_linear > self.max_gear):
            self.gear_linear = self.max_gear
        if(self.gear_linear < -self.max_gear):
            self.gear_linear = -self.max_gear

        if(self.gear_angular > self.max_gear):
            self.gear_angular = self.max_gear
        if(self.gear_angular < -self.max_gear):
            self.gear_angular = -self.max_gear
        
        self.twist.linear.x = self.step * self.gear_linear
        self.twist.linear.y = 0
        self.twist.linear.z = 0
        self.twist.angular.x = 0
        self.twist.angular.y = 0
        self.twist.angular.z = self.step * self.gear_angular
        
        self.pub_twist.publish( self.twist )

    def key_threat_func(self):
        
        while(not rospy.is_shutdown()):
            self.key = self.key_listener.getKey()

            

            if(self.key == "w"):
                    self.gear_linear += 1
            elif(self.key == "a"):
                self.gear_angular += 1
            elif(self.key == "s"):
                self.gear_linear -= 1
            elif(self.key == "d"):
                self.gear_angular -= 1
            elif(self.key == '\x03'):
                exit()
            

            if(self.key in ['a','s','d','w']):
                print("Linear velocity : {} m/s, Angular velocity: {} m/s ".format(self.step*self.gear_linear,self.step * self.gear_angular))
            
            # self.key = None


    def main(self):

        r = rospy.Rate(10) # 10hz 
        while not rospy.is_shutdown():
            self.pubTwist()
            r.sleep()


        

        

    



if __name__ == '__main__':
    
    rospy.init_node('turtlebot_keyboard')

    try:

        while(not rospy.is_shutdown()):
            Teleop_obj = Teleop()
            # rospy.spin()
    finally:
        pass