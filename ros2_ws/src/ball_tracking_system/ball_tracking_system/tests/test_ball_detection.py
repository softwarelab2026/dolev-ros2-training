import pytest
from ball_tracking_system.logic.detector import ball_detection_by_color
from ball_tracking_system.logic.frame import Frame
from ball_tracking_system.logic.ball import Ball
from geometry_msgs.msg import Point


@pytest.mark.unit
def test_ball_detection_for_default_place(frame: Frame, ball: Ball):
    frame.draw_ball(ball)
    assert ball_detection_by_color(frame.data) == Point(x=100.0, y=100.0, z=0.0)
