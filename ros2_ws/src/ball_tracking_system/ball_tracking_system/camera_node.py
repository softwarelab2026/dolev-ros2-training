# camera_sim_node.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np
import cv2


class CameraSimNode(Node):
    def __init__(self):
        super().__init__("camera_sim_node")
        self.publisher_ = self.create_publisher(Image, "/camera/image_raw", 10)
        self.cv_bridge = CvBridge()
        self.timer_period = 0.05  # 20 FPS
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        self.width = 1280
        self.height = 960

        self.ball_pos = [100, 100]  # x, y
        self.ball_vel = [5, 3]  # dx, dy
        self.ball_radius = 40

    def timer_callback(self):
        # Create a white image
        frame = np.ones((self.height, self.width, 3), dtype=np.uint8) * 255

        # Draw the red ball
        cv2.circle(
            frame,
            (int(self.ball_pos[0]), int(self.ball_pos[1])),
            self.ball_radius,
            (0, 0, 255),
            -1,
        )

        # Move the ball
        self.ball_pos[0] += self.ball_vel[0]
        self.ball_pos[1] += self.ball_vel[1]

        # Bounce off walls
        if (
            self.ball_pos[0] - self.ball_radius <= 0
            or self.ball_pos[0] + self.ball_radius >= self.width
        ):
            self.ball_vel[0] *= -1
        if (
            self.ball_pos[1] - self.ball_radius <= 0
            or self.ball_pos[1] + self.ball_radius >= self.height
        ):
            self.ball_vel[1] *= -1

        # Convert to ROS Image message
        image_msg = self.cv_bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        self.publisher_.publish(image_msg)
        self.get_logger().info(f"Publishing frame with ball at {self.ball_pos}")


def main(args=None):
    rclpy.init(args=args)
    node = CameraSimNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
