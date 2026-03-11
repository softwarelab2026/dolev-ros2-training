# subscribe to the ball location node and steer the robot towards the ball with pwd control


from rclpy.node import Node
import rclpy
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from ball_tracking_system.nodes.camera import CameraNode
from ball_tracking_system.utils.mapping import map_coordinate_to_turtlesim_coordinates


class ControlRobotNode(Node):
    def __init__(self):
        super().__init__("control_robot_node")
        self.ball_pose_from_camera: Point = None
        self.turtle_pose: Pose = None
        self.image_width = CameraNode.video_width
        self.image_height = CameraNode.video_height
        self.FPS = CameraNode.FPS

        self.ball_location_sub = self.create_subscription(
            Point, "/ball/location", self.ball_location_callback, 10
        )

        self.turtle_pose_sub = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10
        )

        self.cmd_vel_pub = self.create_publisher(Twist, "/output/cmd_vel", 10)

        self.create_timer(1.0 / self.FPS, self.steer_turtle_position)

    def ball_location_callback(self, msg: Point):
        self.ball_pose_from_camera = msg

    def pose_callback(self, msg: Pose):
        self.turtle_pose = msg

    def steer_turtle_position(self):
        if self.ball_pose_from_camera is None or self.turtle_pose is None:
            return
        twist = Twist()
        # scale the self.ball_pose.x and self.ball_pose y
        ball_x, ball_y = map_coordinate_to_turtlesim_coordinates(
            self.ball_pose_from_camera.x, self.ball_pose_from_camera.y
        )

        error_x = ball_x - self.turtle_pose.x
        error_y = ball_y - self.turtle_pose.y

        self.get_logger().info(
            f"Ball position: ({self.ball_pose_from_camera.x}, {self.ball_pose_from_camera.y}), Turtle position: ({self.turtle_pose.x}, {self.turtle_pose.y}), Error: ({error_x}, {error_y})"
        )

        twist.linear.x = 0.0
        twist.angular.z = 0.0

        self.cmd_vel_pub.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = ControlRobotNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
