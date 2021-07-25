#!/usr/bin/env python

import rospy
import math

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

def PID_Controller(x_target, y_target, pub_obj):
    global x_0, y_0, theta_0
    P_out = Twist()

    K_vel_P = 0.495
    K_vel_I = 7e-7

    K_omega_P = 1.575
    K_omega_I = 1e-9

    t0 = rospy.rostime.Time.now().to_sec()

    dist_integral = 0.0
    theta_integral = 0.0

    while True :
        angle_to_target = math.atan2(y_target - y_0, x_target - x_0)
        dist_to_target = math.sqrt( (x_target - x_0)**2 + (y_target - y_0)**2 )

        angle_error = angle_to_target - theta_0
        distance_error = dist_to_target

        dist_integral = dist_integral + distance_error
        theta_integral = theta_integral + angle_error

        P_out.linear.x = K_vel_P * distance_error + K_vel_I * dist_integral
        P_out.angular.z = K_omega_P * angle_error + K_omega_I * theta_integral

        pub_obj.publish(P_out)
        print('Distance - ', dist_to_target)

        if dist_to_target < 0.5:
            t = rospy.rostime.Time.now().to_sec()
            print('Took ', t - t0, ' sec')
            break

def pose_callback(turtPose):
    global x_0, y_0, theta_0
    x_0 = turtPose.x
    y_0 = turtPose.y
    theta_0 = turtPose.theta

if __name__ == '__main__':
    try:
        rospy.init_node('stMoveComm', anonymous=True)
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        pose_subs = rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
        rospy.sleep(1.0)
        PID_Controller(1.0, 1.0, pub)


    except rospy.ROSInterruptException:
        pass

# 4.7999 sec