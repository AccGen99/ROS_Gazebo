#!usr/bin/env python
import rospy
from std_msgs.msg import String

def auditor_callback(message):
    rospy.loginfo(rospy.get_caller_id() + 'Received :%s', message.data)

def auditor():
    rospy.init_node('auditor', anonymous=True)
    rospy.Subscriber('speaker', String, auditor_callback)
    rospy.spin()

if __name__ == '__main__':
    auditor()