import sys
import rospy
from ros_essentials_cpp.srv import RectangleAreaService
from ros_essentials_cpp.srv import RectangleAreaServiceRequest
from ros_essentials_cpp.srv import RectangleAreaServiceResponse

def RectangleAreaService_client(x, y):
    rospy.wait_for_service('Rectangle_Area_Server')
    try:
        areacalc = rospy.ServiceProxy('Rectangle_Area_Server', RectangleAreaService)
        resp1 = areacalc(x, y)
        return resp1.area
    except rospy.ServiceException(e):
        print("Service call failed: %s"%e)

def usage():
    return

if __name__ == "__main__":
    if len(sys.argy) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print('%s [x y]'%sys.argv[0])
        sys.exit(1)
    print("Requesting %s+%s"%(x, y))
    s = RectangleAreaService_client(x, y)
    print('%s X %s = %s'%(x, y, s))