cmake_minimum_required(VERSION 3.0.2)
project(rospy_tutorial)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)


## Generate messages in the 'msg' folder
add_message_files(
  FILES
  example.msg
  # Message1.msg
  # Message2.msg
)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs  # Or other packages containing msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES bootcamp
#  CATKIN_DEPENDS roscpp rosmsgs rospy
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)




#############
## Install ##
#############

catkin_install_python(PROGRAMS
  001_python_listener_publisher/scripts/pub.py
  001_python_listener_publisher/scripts/sub.py

  002_custom_python_listener_publisher/scripts/custom_msg_pub.py
  002_custom_python_listener_publisher/scripts/custom_msg_sub.py
  
  003_python_listener_publisher_class/scripts/pub_class.py
  003_python_listener_publisher_class/scripts/sub_class.py


  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)