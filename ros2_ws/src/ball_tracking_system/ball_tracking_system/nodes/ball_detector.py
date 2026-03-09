# detects the ball in from the image topic stream and publishes the ball location
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image


class BallDetectorNode(Node):
    def __init__(self):
        super().__init__("ball_detector_node")
        self.image_stream_sub = self.create_subscription(
            Image, "/camera/image_raw", self.image_callback, 10
        )
        self.subscription

    def image_callback(self, msg):
        # frame = msg.data
        # TODO: we are doing some color detection to find the ball x and y
        # we will publish the ball location to a topic called /ball/location
        pass


def main(args=None):
    rclpy.init(args=args)

    ball_detector = BallDetectorNode()

    rclpy.spin(ball_detector)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    ball_detector.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
