# camera_sim_node.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from ball_tracking_system.logic.frame_generator import FrameGenerator


class CameraNode(Node):
    def __init__(self):
        super().__init__("camera_node")
        self.publisher_ = self.create_publisher(Image, "/camera/image_raw", 10)
        self.cv_bridge = CvBridge()
        self.FPS = 10

        self.video_width = 1280
        self.video_height = 960

        self.timer = self.create_timer(1.0 / self.FPS, self.timer_callback)
        self.frame = FrameGenerator(self.video_width, self.video_height, ball_radius=20)

    def timer_callback(self):
        self.frame.move_objects()
        self.frame.generate_frame()

        image_msg = self.cv_bridge.cv2_to_imgmsg(self.frame.data, encoding="bgr8")
        self.publisher_.publish(image_msg)
        self.get_logger().info(f"Publishing frame with ball at {self.frame.ball_pos}")


def main(args=None):
    rclpy.init(args=args)
    node = CameraNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
