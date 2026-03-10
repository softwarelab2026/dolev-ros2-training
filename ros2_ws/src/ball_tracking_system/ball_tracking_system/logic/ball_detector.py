from geometry_msgs.msg import Point
import cv2


def ball_detection_by_color(img, lower_red, upper_red) -> Point:
    hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    red_mask = cv2.inRange(hsvFrame, lower_red, upper_red)

    contours, hierarchy = cv2.findContours(
        red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    if len(contours) == 0:
        raise Exception("Ball not found")

    contour = contours[0]

    (x, y), radius = cv2.minEnclosingCircle(contour)
    print(f"Detected ball at: ({x}, {y}) with radius: {radius}")
    return Point(x=x, y=y, z=0.0)
