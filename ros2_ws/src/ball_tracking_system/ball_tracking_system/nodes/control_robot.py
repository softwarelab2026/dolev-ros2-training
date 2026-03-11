# subscribe to the ball location node and steer the robot towards the ball with pwd control
from rclpy.node import Node
import rclpy
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class ControlRobotNode(Node):
    def __init__(self):
        super().__init__("control_robot_node")
        self.ball_pose: Point = None
        self.turtle_pose: Pose = None

        self.ball_location_sub = self.create_subscription(
            Point, "/ball/location", self.ball_location_callback, 10
        )

        self.turtle_pose_sub = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10
        )
        self.cmd_vel_pub = self.create_publisher(Twist, "/output/cmd_vel", 10)
        self.FPS = 10
        self.create_timer(1.0 / self.FPS, self.steer_turtle_position)

    def ball_location_callback(self, msg: Point):
        self.ball_pose = msg

    def pose_callback(self, msg: Pose):
        self.turtle_pose = msg

    def steer_turtle_position(self):
        twist = Twist()
        twist.linear.x = 5.0
        twist.angular.z = 10.0
        self.cmd_vel_pub.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = ControlRobotNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
