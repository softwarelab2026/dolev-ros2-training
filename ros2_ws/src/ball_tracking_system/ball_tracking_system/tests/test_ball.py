import pytest
from ball_tracking_system.logic.ball import Ball
from ball_tracking_system.logic.frame import Frame


@pytest.mark.unit
def test_ball_movement(ball: Ball, frame: Frame) -> None:
    pos = ball.pos.copy()
    frame.update_position(ball)
    assert ball.pos[0] == pos[0] + ball.vel[0]
    assert ball.pos[1] == pos[1] + ball.vel[1]


@pytest.mark.unit
def test_ball_bounce_vertical_wall(ball: Ball, frame: Frame) -> None:
    ball.pos = [620, 460]  # Near the bottom-right corner
    frame.update_position(ball)
    assert ball.vel[1] == -3


@pytest.mark.unit
def test_ball_bounce_horizontal_wall(ball: Ball, frame: Frame) -> None:
    ball.pos = [620, 460]  # Near the bottom-right corner
    frame.update_position(ball)
    assert ball.vel[0] == -5
