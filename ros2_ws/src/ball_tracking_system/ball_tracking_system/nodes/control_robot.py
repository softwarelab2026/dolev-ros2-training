# subscribe to the ball location node and steer the robot towards the ball with pwd control
from rclpy.node import Node
import rclpy
from geometry_msgs.msg import Point


class ControlRobotNode(Node):
    def __init__(self):
        super().__init__("control_robot_node")
        self.ball_location_sub = self.create_subscription(
            Point, "/ball/location", self.ball_location_callback, 10
        )

    def ball_location_callback(self, msg: Point):
        self.get_logger().info(f"Received ball location: x={msg.x}, y={msg.y}")


def main(args=None):
    rclpy.init(args=args)
    node = ControlRobotNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
