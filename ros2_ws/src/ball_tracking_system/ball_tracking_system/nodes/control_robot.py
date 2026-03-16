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
        self._ball_pose_from_camera: Point = None
        self._turtle_pose: Pose = None
        self._image_width = CameraNode.video_width
        self._image_height = CameraNode.video_height
        self._FPS = CameraNode.FPS

        self._linear_pid = PID(kp=1.5, ki=0.0, kd=0.2)
        self._angular_pid = PID(kp=4.0, ki=0.0, kd=0.5)

        self._previous_time = self.get_clock().now()

        self._ball_location_sub = self.create_subscription(
            Point, "/ball/location", self._ball_location_callback, 10
        )

        self._turtle_pose_sub = self.create_subscription(
            Pose, "/turtle1/pose", self._pose_callback, 10
        )

        self._cmd_vel_pub = self.create_publisher(Twist, "/output/cmd_vel", 10)

        self.create_timer(1.0 / self._FPS, self._steer_turtle_position)

    def _ball_location_callback(self, msg: Point):
        self._ball_pose_from_camera = msg

    def _pose_callback(self, msg: Pose):
        self._turtle_pose = msg

    def _steer_turtle_position(self):
        if self._ball_pose_from_camera is None or self._turtle_pose is None:
            return

        ball_x, ball_y = map_coordinate_to_turtlesim_coordinates(
            self._ball_pose_from_camera.x,
            self._ball_pose_from_camera.y,
            self._image_width,
            self._image_height,
        )

        current_time = self.get_clock().now()
        duration = current_time - self._previous_time
        dt = duration.nanoseconds / 1e9
        self._previous_time = current_time
        

        twist = calculate_velocity_to_ball(
            self._turtle_pose, ball_x, ball_y, self._linear_pid, self._angular_pid, dt
        )

        self._cmd_vel_pub.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = ControlRobotNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
