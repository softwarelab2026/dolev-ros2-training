import pytest
from ball_tracking_system.logic.ball_detector import ball_detection_by_color
from ball_tracking_system.logic.frame_generator import generate_frame
from ball_tracking_system.logic.ball import Ball
from geometry_msgs.msg import Point


@pytest.mark.unit
def test_raise_exception_ball_not_found_when_no_ball_in_frame(frame_without_ball, lower_red, upper_red
) -> None:
    
    with pytest.raises(Exception):
        ball_detection_by_color(frame_without_ball, lower_red, upper_red)


@pytest.mark.unit
def test_ball_detection_for_default_place(
    frame, lower_red, upper_red
) -> None:
    
    fake_point = Point(x=320.0, y=240.0, z=0.0)
    detected_point = ball_detection_by_color(frame, lower_red, upper_red)

    assert detected_point.x == fake_point.x and detected_point.y == fake_point.y


@pytest.mark.unit
def test_ball_detection_for_moved_by_velocity(
    lower_red, upper_red
) -> None:
    width, height = 640, 480
    ball = Ball(width, height, ball_radius=20, ball_vel_x=5, ball_vel_y=3)
    ball.move_objects()
    frame = generate_frame(width, height, ball.ball_pos, ball.ball_radius)
    
    detected_point = ball_detection_by_color(frame, lower_red, upper_red)
    fake_point = Point(x=325.0, y=243.0, z=0.0)

    assert detected_point.x == fake_point.x and detected_point.y == fake_point.y


@pytest.mark.unit
def test_ball_detection_for_moved_after_x_times(
    lower_red, upper_red
) -> None:
    width, height = 640, 480
    ball = Ball(width, height, ball_radius=20, ball_vel_x=5, ball_vel_y=3)

    ball.move_objects()
    ball.move_objects()
    ball.move_objects()

    frame = generate_frame(width, height, ball.ball_pos, ball.ball_radius)

    detected_point = ball_detection_by_color(frame, lower_red, upper_red)
    
    fake_point = Point(x=335.0, y=249.0, z=0.0)

    assert detected_point.x == fake_point.x and detected_point.y == fake_point.y
