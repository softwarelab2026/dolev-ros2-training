# camera_sim_node.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ball_tracking_system.logic.frame_generator import FrameGenerator

cv_bridge = CvBridge()


class CameraNode(Node):
    video_width = 500
    video_height = 500
    FPS = 10

    def __init__(self):
        super().__init__("camera_node")
        self.image_publisher = self.create_publisher(Image, "/camera/image_raw", 10)

        self.timer = self.create_timer(1.0 / self.FPS, self._publish_image)
        self.frame = FrameGenerator(self.video_width, self.video_height, ball_radius=20)

    def _publish_image(self):
        self.frame.move_objects()
        self.frame.generate_frame()
        self.image_publisher.publish(
            cv_bridge.cv2_to_imgmsg(self.frame.data, encoding="bgr8")
        )
        self.get_logger().info(
            f"The frame was generate the ball location is {self.frame.ball_pos}"
        )


def main(args=None):
    rclpy.init(args=args)
    node = CameraNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
