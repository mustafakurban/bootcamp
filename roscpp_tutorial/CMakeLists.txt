cmake_minimum_required(VERSION 3.0.2)
project(roscpp_tutorial)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)

###################################
## catkin specific configuration ##
###################################

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

add_executable(talker_cpp 001_cpp_listener_publisher/src/pub.cpp)
target_link_libraries(talker_cpp ${catkin_LIBRARIES})
# add_dependencies(talker catkin_EXPORTED_TARGETS)

add_executable(listener_cpp 001_cpp_listener_publisher/src/sub.cpp)
target_link_libraries(listener_cpp ${catkin_LIBRARIES})
# add_dependencies(listener catkin_EXPORTED_TARGETS)
