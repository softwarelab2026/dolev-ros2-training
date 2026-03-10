from geometry_msgs.msg import Point
from sensor_msgs.msg import Image


def ball_detection_by_color(frame: Image) -> Point:
    return Point(x=100.0, y=100.0, z=0.0)
