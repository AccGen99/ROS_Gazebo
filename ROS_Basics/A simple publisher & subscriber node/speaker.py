#!usr/bin/env python
# The shebang line written above ensures that the interpreter used is the first one listed in the PATH variable

import rospy    # Importing rospy for creating speaker node
from std_msgs.msg import String

# When creating a publisher node, first create a publisher object
def speaker():
    pub = rospy.Publisher('speaker', String, queue_size=5)
    rospy.init_node('speaker', anonymous=True)  # If two nodes with same name are launched, the first one is terminated. The anonymous=True
    rate = rospy.Rate(2)                        # ensures this doesn't happen by attaching a unique ID to each new node with a same name
    i = 0

    while not rospy.is_shutdown():
        spkr_msg = 'Hearing message #%s' % i
        rospy.loginfo(spkr_msg)
        pub.publish(spkr_msg)
        rate.sleep()
        i = i + 1

if __name__ == '__main__':
    try:
        speaker()
    except rospy.ROSInterruptException:
        pass