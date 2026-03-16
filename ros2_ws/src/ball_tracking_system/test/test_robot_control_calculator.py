from ball_tracking_system.logic.robot_control_calculator import map_coordinate_to_turtlesim_coordinates, calculate_velocity_to_ball
import pytest

import math


class FakePID:
    def __init__(self, output):
        self.output = output
        self.last_input = None

    def compute(self, value):
        return self.output


class FakePose:
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta

        



@pytest.mark.unit
def test_mapping_coordinates_to_the_middle_of_turtlesim_screen():
    x,y = map_coordinate_to_turtlesim_coordinates(200, 200, 400, 400)
    assert x == 5.5 and y == 5.5

@pytest.mark.unit
def test_mapping_coordinates_to_the_right_top_corner_of_turtlesim_screen():
    x,y = map_coordinate_to_turtlesim_coordinates(400, 400, 400, 400)
    assert x == 11 and y == 0


@pytest.mark.unit
def test_mapping_coordinates_to_the_left_bottom_corner_of_turtlesim_screen():
    x,y = map_coordinate_to_turtlesim_coordinates(0, 0, 400, 400)
    assert x == 0 and y == 11


@pytest.mark.unit
def test_mapping_coordinates_to_the_right_bottom_corner_of_turtlesim_screen():
    x,y = map_coordinate_to_turtlesim_coordinates(400, 0, 400, 400)
    assert x == 11 and y == 11
    

@pytest.mark.unit
def test_velocity_to_ball():
    pose = FakePose(0, 0, 0)

    linear_pid = FakePID(2.0)
    angular_pid = FakePID(0.5)

    twist = calculate_velocity_to_ball(
        pose,
        ball_x=1,
        ball_y=0,
        linear_pid=linear_pid,
        angular_pid=angular_pid,
    )


    # check outputs
    assert twist.linear.x == 2.0
    assert twist.angular.z == 0.5



