#!/usr/bin/env python

import rospy
import math

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

def P_Controller(x_target, y_target, pub_obj):
    global x_0, y_0, theta_0
    P_out = Twist()
    K_vel = 0.55
    K_omega = 1.75
    t0 = rospy.rostime.Time.now().to_sec()

    while True :
        angle_to_target = math.atan2(y_target - y_0, x_target - x_0)
        dist_to_target = math.sqrt( (x_target - x_0)**2 + (y_target - y_0)**2 )

        P_out.linear.x = K_vel * dist_to_target 
        P_out.angular.z = K_omega * (angle_to_target - theta_0)
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
        P_Controller(1.0, 1.0, pub)


    except rospy.ROSInterruptException:
        pass

# 5.382 sec