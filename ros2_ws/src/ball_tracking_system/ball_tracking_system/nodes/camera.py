# camera_sim_node.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ball_tracking_system.logic.ball import Ball
from ball_tracking_system.logic.frame import Frame


class CameraSimNode(Node):
    def __init__(self):
        super().__init__("camera_sim_node")
        self.publisher_ = self.create_publisher(Image, "/camera/image_raw", 10)
        self.cv_bridge = CvBridge()
        self.FPS = 10
        self.video_width = 1280
        self.video_height = 960
        self.timer = self.create_timer(1.0 / self.FPS, self.timer_callback)
        self.ball = Ball(x=100, y=100, radius=40, vx=5, vy=3)

    def timer_callback(self):
        frame = Frame(self.video_width, self.video_height)
        frame.draw_ball(self.ball)

        self.ball.update_position(self.video_width, self.video_height)

        # Convert to ROS Image message
        image_msg = self.cv_bridge.cv2_to_imgmsg(frame.data, encoding="bgr8")
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
