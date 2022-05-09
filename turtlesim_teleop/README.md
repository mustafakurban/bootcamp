NAVIGATING TURTLEBOT3 WITH KEYBOARD

Clone this repository and run firstly `roscore` . 

In order to start simulation use `roslaunch` . 
BUT DON'T FORGET TO CONFIGURE launch_world.launch file in line 8:

`<arg name="world" value="YOUR_OWN_PATH/turtlesim_teleop/worlds/area.wbt"/>`

After doing required changes run `roslaunch turtlesim_teleop launch_world.launch` .

The simulation will be start and you can control the turtlebot3 with keyboard.

But don't forget that you must push keyboard while your launch terminal is been selected.