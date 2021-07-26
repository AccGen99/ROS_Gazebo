'''
A cleaning application implemented in turtlesim simulator
and ROS Noetic Ninjemys framework

To execute, launch the launcher.launch file

Turtlebot first moves to (1,1) from spawn location, then
performs cleaning action by following grid cleaning 
pattern. The pattern can be changed to spiral by 
uncommenting the spiralClean function and commenting
the gridClean function in try block.
'''

#!/usr/bin/env python

import rospy
import math

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

def gridClean(pub, currSp):
    PID_Controller(1.0, 1.0, pub)
    rotate(270, pub)
    for i in range(8):
        moveStraight(9.0, currSp, pub)
        rotate(0, pub)
        moveStraight(1.0, currSp, pub)
        rotate(-90, pub)
        moveStraight(9.0, currSp, pub)
        rotate(0, pub)
        moveStraight(1.0, currSp, pub)
        rotate(90, pub)

def rotate(angle, pub):
    message_object = Twist()
    angle_rads = angle*3.14/180
    t0 = rospy.rostime.Time.now().to_sec()

    while True:
        t = rospy.rostime.Time.now().to_sec()
        angle_new = (theta_0 + 1.5 * (t - t0)) % 360
        message_object.angular.z = 1.5
        rate = rospy.Rate(1)
        pub.publish(message_object)
        rate.sleep()
        if abs(angle_new - angle_rads) > 0.1:
            break



def moveStraight(reqdDist, currSp, pub):
    msg_obj = Twist()
    msg_obj.linear.x = abs(currSp)

    turtLocX = 0.0
    turtLocY = 0.0

    t0 = rospy.rostime.Time.now().to_sec()
    dist_trav = 0.0

    while dist_trav < reqdDist:
        t = rospy.rostime.Time.now().to_sec()
        dist_trav = currSp * (t - t0)
        rate = rospy.Rate(1)
        pub.publish(msg_obj)
        rate.sleep()


def PID_Controller(x_target, y_target, pub_obj):
    global x_0, y_0, theta_0
    P_out = Twist()

    K_vel_P = 0.66
    K_vel_I = 4.2e-7
    K_vel_D = 8e-7

    K_omega_P = 2.1
    K_omega_I = 0.6e-9
    K_omega_D = 0.15e-9

    t0 = rospy.rostime.Time.now().to_sec()
    dist_integral = 0.0
    theta_integral = 0.0

    while True :
        angle_to_target = math.atan2(y_target - y_0, x_target - x_0)
        dist_to_target = math.sqrt( (x_target - x_0)**2 + (y_target - y_0)**2 )

        angle_derivative = velocity_ang
        distance_derivative = velocity_lin

        angle_error = angle_to_target - theta_0
        distance_error = dist_to_target

        dist_integral = dist_integral + distance_error
        theta_integral = theta_integral + angle_error

        P_out.linear.x = K_vel_P * distance_error + K_vel_I * dist_integral + K_vel_D * distance_derivative
        P_out.angular.z = K_omega_P * angle_error + K_omega_I * theta_integral + K_omega_D * angle_derivative

        pub_obj.publish(P_out)
        #print('Distance - ', dist_to_target)

        if dist_to_target < 0.5:
            #t = rospy.rostime.Time.now().to_sec()
            #print('Took ', t - t0, ' sec')
            break

def pose_callback(turtPose):
    global x_0, y_0, theta_0
    global velocity_lin, velocity_ang
    x_0 = turtPose.x
    y_0 = turtPose.y
    theta_0 = turtPose.theta
    velocity_lin = turtPose.linear_velocity
    velocity_ang = turtPose.angular_velocity


if __name__ == '__main__':
    try:
        rospy.init_node('stMoveComm', anonymous=True)
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        pose_subs = rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
        rospy.sleep(1.0)
        gridClean(pub, 3.0)


    except rospy.ROSInterruptException:
        pass

# 4.075 sec