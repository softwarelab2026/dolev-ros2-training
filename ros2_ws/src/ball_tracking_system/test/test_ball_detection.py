import pytest
from ball_tracking_system.logic.ball_detector import ball_detection_by_color
from ball_tracking_system.logic.frame_generator import FrameGenerator

from geometry_msgs.msg import Point


@pytest.mark.unit
def test_raise_exception_ball_not_found_when_no_ball_in_frame(
    frame_generator: FrameGenerator, lower_red, upper_red
) -> None:
    with pytest.raises(Exception):
        ball_detection_by_color(frame_generator.data, lower_red, upper_red)


@pytest.mark.unit
def test_ball_detection_for_default_place(
    frame_generator: FrameGenerator, lower_red, upper_red
) -> None:
    frame = frame_generator.generate_frame()
    fake_point = Point(x=320.0, y=240.0, z=0.0)
    detected_point = ball_detection_by_color(frame, lower_red, upper_red)

    assert detected_point.x == fake_point.x and detected_point.y == fake_point.y


@pytest.mark.unit
def test_ball_detection_for_moved_by_velocity(
    frame_generator: FrameGenerator, lower_red, upper_red
) -> None:
    frame_generator.move_objects()
    frame = frame_generator.generate_frame()

    detected_point = ball_detection_by_color(frame, lower_red, upper_red)
    fake_point = Point(x=325.0, y=243.0, z=0.0)

    assert detected_point.x == fake_point.x and detected_point.y == fake_point.y


@pytest.mark.unit
def test_ball_detection_for_moved_place(
    frame_generator: FrameGenerator, lower_red, upper_red
) -> None:
    frame_generator.ball_pos = [200.0, 150.0]
    frame_generator.move_objects()

    frame = frame_generator.generate_frame()
    detected_point = ball_detection_by_color(frame, lower_red, upper_red)
    
    fake_point = Point(x=205.0, y=153.0, z=0.0)

    assert detected_point.x == fake_point.x and detected_point.y == fake_point.y
