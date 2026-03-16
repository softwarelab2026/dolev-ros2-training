from ball_tracking_system.logic.robot_control_calculator import map_coordinate_to_turtlesim_coordinates, calculate_velocity_to_ball
import pytest


from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

def test_mapping_coordinates_to_the_middle_of_turtlesim_screen():
    x,y = map_coordinate_to_turtlesim_coordinates(200, 200, 400, 400)
    assert x == 5.5 and y == 5.5


def test_mapping_coordinates_to_the_right_top_corner_of_turtlesim_screen():
    x,y = map_coordinate_to_turtlesim_coordinates(400, 400, 400, 400)
    assert x == 11 and y == 0



def test_mapping_coordinates_to_the_left_bottom_corner_of_turtlesim_screen():
    x,y = map_coordinate_to_turtlesim_coordinates(0, 0, 400, 400)
    assert x == 0 and y == 11



def test_mapping_coordinates_to_the_right_bottom_corner_of_turtlesim_screen():
    x,y = map_coordinate_to_turtlesim_coordinates(400, 0, 400, 400)
    assert x == 11 and y == 11
    


def test_velocity_to_ball_when_turtle_same_y_with_ball(simple_pid):
    pose = Pose()
    pose.x = 0.0
    pose.y = 0.0
    


    twist = calculate_velocity_to_ball(
        pose,
        ball_x=1,
        ball_y=0,
        linear_pid=simple_pid,
        angular_pid=simple_pid,
        dt=1
    )


    # check outputs
    assert twist.linear.x == 1.0
    

def test_velocity_to_ball_when_turtle_same_x_with_ball(simple_pid):
    pose = Pose()
    pose.x = 0.0
    pose.y = 10.0

    twist = calculate_velocity_to_ball(
        pose,
        ball_x=0.0,
        ball_y=11.0,
        linear_pid=simple_pid,
        angular_pid=simple_pid,
        dt=1
    )
    assert twist.linear.x == 1
    

def test_velocity_to_ball_when_turtle_on_different_x_and_y(simple_pid):
    pose = Pose()
    pose.x = 0.0
    pose.y = 10.0

    twist = calculate_velocity_to_ball(
        pose,
        ball_x=5.0,
        ball_y=11.0,
        linear_pid=simple_pid,
        angular_pid=simple_pid,
        dt=1
    )
    
    assert pytest.approx(twist.linear.x == 5)
    assert pytest.approx(twist.linear.y == 1)


def test_angular_velocity_to_ball_when_ball_is_45_degrees_from_turtle(simple_pid):
    pose = Pose()
    pose.x = 0.0
    pose.y = 0.0
 
    twist = calculate_velocity_to_ball(
        pose,
        ball_x=1.0,
        ball_y=1.0,
        linear_pid=simple_pid,
        angular_pid=simple_pid,
        dt=1
    )
    
    assert pytest.approx(twist.angular.z == math.radians(45))


def test_angular_velocity_to_ball_when_ball_is_135_degrees_from_turtle(simple_pid):
    pose = Pose()
    pose.x = 5.0
    pose.y = 5.0

    twist = calculate_velocity_to_ball(
        pose, 
        ball_x=4.0,
        ball_y=6.0,
        linear_pid=simple_pid,
        angular_pid=simple_pid,
        dt=1
    )
    assert pytest.approx(twist.angular.z == math.radians(135))

def test_angular_velocity_to_ball_when_ball_is_270_degrees_do_normalize_so_it_will_be_negative_90(simple_pid):
    pose = Pose()
    pose.x = 5.0
    pose.y = 5.0

    twist = calculate_velocity_to_ball(
        pose, 
        ball_x=6.0,
        ball_y=4.0,
        linear_pid=simple_pid,
        angular_pid=simple_pid,
        dt=1
    )

    assert pytest.approx(twist.angular.z == math.radians(-90))







