import pytest
from ball_tracking_system.logic.ball_detector import ball_detection_by_color
from ball_tracking_system.logic.frame import Frame
from ball_tracking_system.logic.ball import Ball
from geometry_msgs.msg import Point
import numpy as np


@pytest.mark.unit
def test_raise_exception_ball_not_found_when_no_ball_in_frame(frame: Frame) -> None:
    with pytest.raises(Exception, match="Ball not found"):
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])
        ball_detection_by_color(frame.data, lower_red, upper_red)


@pytest.mark.unit
def test_ball_detection_for_default_place(frame: Frame, ball: Ball) -> None:
    frame.draw_ball(ball)
    fake_point = Point(x=100.0, y=100.0, z=0.0)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    detected_point = ball_detection_by_color(frame.data, lower_red, upper_red)

    assert detected_point.x == fake_point.x and detected_point.y == fake_point.y


@pytest.mark.unit
def test_ball_detection_for_moved_by_velocity(frame: Frame, ball: Ball) -> None:
    ball.move_by_velocity()
    frame.draw_ball(ball)

    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    detected_point = ball_detection_by_color(frame.data, lower_red, upper_red)
    fake_point = Point(x=105.0, y=103.0, z=0.0)

    assert detected_point.x == fake_point.x and detected_point.y == fake_point.y


@pytest.mark.unit
def test_ball_detection_for_moved_place(frame: Frame, ball: Ball) -> None:
    ball.set_position(200, 150)
    frame.draw_ball(ball)

    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    detected_point = ball_detection_by_color(frame.data, lower_red, upper_red)

    fake_point = Point(x=200.0, y=150.0, z=0.0)
    assert detected_point.x == fake_point.x and detected_point.y == fake_point.y
