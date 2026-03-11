import math
from geometry_msgs.msg import Pose, Twist

from ball_tracking_system.logic.pid_controller import PID


def map_coordinate_to_turtlesim_coordinates(x, y, video_width, video_height):
    new_x = (x / video_width) * 11.0
    new_y = ((video_height - y) / video_height) * 11.0
    return new_x, new_y


def normalize_angle(angle):
    return math.atan2(math.sin(angle), math.cos(angle))


def calculate_velocity_to_ball(
    turtle_pose: Pose, ball_x, ball_y, linear_pid: PID, angular_pid: PID
) -> Twist:
    dx = ball_x - turtle_pose.x
    dy = ball_y - turtle_pose.y

    distance_error = math.sqrt(dx**2 + dy**2)

    angle_to_ball = math.atan2(dy, dx)
    angle_error = normalize_angle(angle_to_ball - turtle_pose.theta)

    linear_speed = linear_pid.compute(distance_error)
    angular_speed = angular_pid.compute(angle_error)

    twist = Twist()
    twist.linear.x = linear_speed
    twist.angular.z = angular_speed
    return twist
