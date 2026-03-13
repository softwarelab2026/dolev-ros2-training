# subscribe to the ball location node and steer the robot towards the ball with pwd control


from rclpy.node import Node
import rclpy
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from ball_tracking_system.nodes.camera import CameraNode
from ball_tracking_system.logic.pid_controller import PID
from ball_tracking_system.logic.robot_control_calculator import (
    calculate_velocity_to_ball,
    map_coordinate_to_turtlesim_coordinates,
)


class ControlRobotNode(Node):
    def __init__(self):
        super().__init__("control_robot_node")
        self.ball_pose_from_camera: Point = None
        self.turtle_pose: Pose = None
        self.image_width = CameraNode.video_width
        self.image_height = CameraNode.video_height
        self.FPS = CameraNode.FPS

        self.linear_pid = PID(kp=1.5, ki=0.0, kd=0.2)
        self.angular_pid = PID(kp=4.0, ki=0.0, kd=0.5)

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

        # scale the self.ball_pose.x and self.ball_pose y
        ball_x, ball_y = map_coordinate_to_turtlesim_coordinates(
            self.ball_pose_from_camera.x,
            self.ball_pose_from_camera.y,
            self.image_width,
            self.image_height,
        )

        twist = calculate_velocity_to_ball(
            self.turtle_pose, ball_x, ball_y, self.linear_pid, self.angular_pid
        )
        self.cmd_vel_pub.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = ControlRobotNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
