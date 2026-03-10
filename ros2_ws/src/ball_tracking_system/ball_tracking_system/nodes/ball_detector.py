# detects the ball in from the image topic stream and publishes the ball location
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from ball_tracking_system.logic import ball_detector
from cv_bridge import CvBridge


bridge = CvBridge()


class BallDetectorNode(Node):
    def __init__(self):
        super().__init__("ball_detector_node")
        self.image_stream_sub = self.create_subscription(
            Image, "/camera/image_raw", self.image_callback, 10
        )
        self.image_stream_sub
        self.ball_location_pub = self.create_publisher(Point, "/ball/location", 10)

    def image_callback(self, msg: Image):
        np_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

        location = ball_detector.ball_detection_by_color(np_image)
        self.ball_location_pub.publish(location)


def main(args=None):
    rclpy.init(args=args)
    ball_detector = BallDetectorNode()
    rclpy.spin(ball_detector)

    ball_detector.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
