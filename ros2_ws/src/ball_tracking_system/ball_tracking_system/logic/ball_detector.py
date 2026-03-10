from geometry_msgs.msg import Point
import cv2
import numpy as np


def ball_detection_by_color(img) -> Point:
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Mask
    red_mask = cv2.inRange(hsvFrame, lower_red, upper_red)

    contours, hierarchy = cv2.findContours(
        red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )
    if len(contours) == 0:
        raise Exception("Ball not found")
    # get the first contour

    contour = contours[0]

    (x, y), radius = cv2.minEnclosingCircle(contour)
    print(f"Detected ball at: ({x}, {y}) with radius: {radius}")
    return Point(x=x, y=y, z=0.0)
