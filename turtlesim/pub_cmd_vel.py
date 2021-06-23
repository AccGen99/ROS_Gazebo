# Publish command to Turtlebot topic cmd_vel

#!usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def pub_cmd_vel():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=5)
    rospy.init_node('pub_cmd_vel', anonymous=False)
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 0.5
        twist.angular.z = 0.5
        spkr_msg = twist
        rospy.loginfo(spkr_msg)
        pub.publish(spkr_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        pub_cmd_vel()
    except rospy.ROSInterruptException:
        pass