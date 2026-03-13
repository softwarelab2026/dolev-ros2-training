from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="ball_tracking_system",
                executable="camera_node",
                name="camera_node",
            ),
            Node(
                package="ball_tracking_system",
                executable="ball_detector_node",
                name="ball_detector_node",
            ),
            Node(
                package="rqt_gui",
                executable="rqt_gui",
                name="rqt_gui",
            ),
            Node(
                package="turtlesim",
                executable="turtlesim_node",
                name="sim",
            ),
            Node(
                package="ball_tracking_system",
                executable="control_robot_node",
                name="control_robot_node",
                remappings=[
                    ("/output/cmd_vel", "/turtle1/cmd_vel"),
                ],
            ),
        ]
    )
