# Subscribes to the topic turtle1/pose
# Prints position of the robot

#!usr/bin/env python
import rospy
from turtlesim.msg import Pose

def pose_callback(message):
    rospy.loginfo(rospy.get_caller_id() + 'x - %s, y - %s, theta - %s, l_vel - %s, ang_vel - %s', message.x, message.y, message.theta, message.linear_velocity, message.angular_velocity)

def turtlesim_pose():
    rospy.init_node('turtlesim_pose', anonymous=True)
    rospy.Subscriber('turtle1/pose', Pose, pose_callback)
    rospy.spin()

if __name__ == '__main__':
    turtlesim_pose()