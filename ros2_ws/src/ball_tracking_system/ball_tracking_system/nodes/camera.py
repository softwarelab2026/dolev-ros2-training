# camera_sim_node.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np
from ball_tracking_system.logic.ball import Ball
import cv2


class CameraSimNode(Node):
    def __init__(self):
        super().__init__("camera_sim_node")
        self.publisher_ = self.create_publisher(Image, "/camera/image_raw", 10)
        self.cv_bridge = CvBridge()
        self.FPS = 60

        self.timer = self.create_timer(1.0 / self.FPS, self.timer_callback)
        self.ball = Ball(x=100, y=100, radius=40, vx=5, vy=3, width=1280, height=960)

    def timer_callback(self):
        # Create a white image
        frame = np.ones((self.ball.height, self.ball.width, 3), dtype=np.uint8) * 255

        cv2.circle(
            frame,
            (int(self.ball.pos[0]), int(self.ball.pos[1])),
            self.ball.radius,
            (0, 0, 255),
            -1,
        )

        self.ball.update_position()

        # Convert to ROS Image message
        image_msg = self.cv_bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        self.publisher_.publish(image_msg)
        self.get_logger().info(f"Publishing frame with ball at {self.ball.pos}")


def main(args=None):
    rclpy.init(args=args)
    node = CameraSimNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
