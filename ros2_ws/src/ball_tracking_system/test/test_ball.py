import pytest
from ball_tracking_system.logic.ball import Ball
from ball_tracking_system.logic.frame import Frame


@pytest.mark.unit
def test_ball_movement_by_velocity(ball: Ball, frame: Frame) -> None:
    pos = ball.pos.copy()
    ball.update_position(frame.width, frame.height)

    assert ball.pos[0] == pos[0] + 5
    assert ball.pos[1] == pos[1] + 3


@pytest.mark.unit
def test_ball_bounce_vertical_wall(ball: Ball, frame: Frame) -> None:
    ball.pos = [620, 460]  # Near the bottom-right corner
    ball.update_position(frame.width, frame.height)
    assert ball.vel[1] == -3


@pytest.mark.unit
def test_ball_bounce_horizontal_wall(ball: Ball, frame: Frame) -> None:
    ball.pos = [620, 460]  # Near the bottom-right corner
    ball.update_position(frame.width, frame.height)
    assert ball.vel[0] == -5
