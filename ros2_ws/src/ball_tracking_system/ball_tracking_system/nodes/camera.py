# camera_sim_node.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ball_tracking_system.logic.frame_generator import generate_frame
from ball_tracking_system.logic.ball import Ball


cv_bridge = CvBridge()

cv_bridge = CvBridge()


class CameraNode(Node):
    video_width = 1280
    video_height = 960
    FPS = 10

    def __init__(self):
        super().__init__("camera_sim_node")
        self._camera_publisher = self.create_publisher(Image, "/camera/image_raw", 10)

        self._FPS = 10

        self._timer = self.create_timer(1.0 / self._FPS, self._timer_callback)
        self._ball = Ball(
            self.video_width,
            self.video_height,
            radius=20,
            vel_x=5,
            vel_y=3,
        )

    def _timer_callback(self):
        self._ball.move_objects()
        generated_frame = generate_frame(
            self.video_width,
            self.video_height,
            self._ball.pos,
            self._ball.radius,
        )

        image_msg = cv_bridge.cv2_to_imgmsg(generated_frame, encoding="bgr8")
        self._camera_publisher.publish(image_msg)
        self.get_logger().info(f"Publishing frame with ball at {self._ball.pos}")


def main(args=None):
    rclpy.init(args=args)
    node = CameraNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
