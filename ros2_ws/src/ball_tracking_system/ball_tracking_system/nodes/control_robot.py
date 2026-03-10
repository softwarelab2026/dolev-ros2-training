# subscribe to the ball location node and steer the robot towards the ball with pwd control
from rclpy.node import Node


class ControlRobotNode(Node):
    def __init__(self):
        super().__init__("control_robot_node")
        # TODO: subscribe to the ball location topic and steer the robot towards the ball with pwd control
