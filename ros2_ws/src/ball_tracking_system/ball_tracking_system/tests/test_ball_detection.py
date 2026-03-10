import pytest
from ball_tracking_system.logic.detector import ball_detection_by_color
from ball_tracking_system.logic.frame import Frame
from ball_tracking_system.logic.ball import Ball
from geometry_msgs.msg import Point


@pytest.mark.unit
def test_ball_detection_for_default_place(frame: Frame, ball: Ball):
    frame.draw_ball(ball)
    fake_point = Point(x=100.0, y=100.0, z=0.0)
    detected_point = ball_detection_by_color(frame.data)

    assert detected_point.x == fake_point.x and detected_point.y == fake_point.y


@pytest.mark.unit
def test_ball_detection_for_moved_by_velocity(frame: Frame, ball: Ball):
    ball.move_by_velocity()
    frame.draw_ball(ball)

    detected_point = ball_detection_by_color(frame.data)
    fake_point = Point(x=105.0, y=103.0, z=0.0)

    assert detected_point.x == fake_point.x and detected_point.y == fake_point.y


@pytest.mark.unit
def test_ball_detection_for_moved_place(frame: Frame, ball: Ball):
    ball.set_position(200, 150)
    frame.draw_ball(ball)

    detected_point = ball_detection_by_color(frame.data)
    fake_point = Point(x=200.0, y=150.0, z=0.0)
    assert detected_point.x == fake_point.x and detected_point.y == fake_point.y
