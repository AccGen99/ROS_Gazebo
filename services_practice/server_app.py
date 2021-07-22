#!/usr/bin/env python
from ros_essentials_cpp.srv import RectangleAreaService
from ros_essentials_cpp.srv import RectangleAreaServiceRequest
from ros_essentials_cpp.srv import RectangleAreaServiceResponse

import rospy

def handle_area(req):
    print("Returning [%s X %s = %s]"%(req.a, req.b, (req.a * req.b)))
    return RectangleAreaServiceResponse(req.a + req.b)

def Rectangle_Area_server():
    rospy.init_node('Rectangle_Area_Server')
    s = rospy.Service('Rectangle_Area_Server', RectangleAreaService, handle_area) # service_name, service_type, handler_function
    print("Ready to calculate area")
    rospy.spin()

if __name__ == "__main__":
    Rectangle_Area_server()