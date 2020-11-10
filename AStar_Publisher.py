#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publish():

    pub     = rospy.Publisher('string_publish', String, queue_size=10)

    rate    = rospy.Rate(1)

    msg_to_publish = String()

    while not rospy.is_shutdown():

        start = raw_input("Type word to solve:  ")
        end = raw_input("Type goal:  ")

        msg = start + "." + end

        msg_to_publish.data = msg
        pub.publish(msg_to_publish)

        rospy.loginfo(msg)

        rate.sleep()

if __name__ == "__main__":
    rospy.init_node("simple_publisher")
    publish()