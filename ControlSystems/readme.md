# Simulation of linear controller on turtlebot using ROS

The following controllers (coded in given files) were implemented on turtlebot in ROS Noetic - 

**P_Controller.py** - Implementation of Proportional controller on turtlebot simulated on turtlesim. Uses a K_p value of 0.55 for velocity and 1.75 for angular velocity. Reaches the position (1,1) from default spawn location in 5.382 sec

**PI_Controller.py** - Implementation of Proportional-Integral controller on turtlebot simulated on turtlesim. K_p values for velocity and angular rate determined using Ziegler-Nichols tuning rules. K_i values determined by hit & trial. Reaches (1,1) from default spawn location in 4.8 sec

**PID_Controller.py** - Implementation of Proportional-Integral-Derivative controller on turtlebot simulated on turtlesim. K_p, K_i and K_d values for velocity and angular rate determined using Ziegler-Nichols tuning rules. K_d values were further tuned for optimal performance. Reaches (1,1) from spawn location in 4.075 sec
