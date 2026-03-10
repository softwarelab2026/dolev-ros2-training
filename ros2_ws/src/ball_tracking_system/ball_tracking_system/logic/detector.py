from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from geometry_msgs.msg import Point
import cv2
import numpy as np

bridge = CvBridge()


def ball_detection_by_color(frame: Image) -> Point:
    img = bridge.imgmsg_to_cv2(frame, desired_encoding="bgr8")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Reduce noise
    gray = cv2.medianBlur(gray, 5)

    # Detect circles
    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=100,
        param1=100,
        param2=40,
        minRadius=30,
        maxRadius=60,
    )
    if not circles:
        raise ValueError("No circles detected in the image.")

    if circles is not None:
        circles = np.uint16(np.around(circles))
        x, y, r = circles[0][0]
        return Point(x=float(x), y=float(y), z=0.0)
