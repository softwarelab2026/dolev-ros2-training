import pytest
from logic.ball import Ball


@pytest.mark.unit
def test_ball_movement(ball: Ball) -> None:
    pos = ball.pos.copy()
    ball.update_position()
    assert ball.pos[0] == pos[0] + ball.vel[0]
    assert ball.pos[1] == pos[1] + ball.vel[1]


@pytest.mark.unit
def test_ball_bounce_vertical_wall(ball: Ball) -> None:
    ball.pos = [620, 460]  # Near the bottom-right corner
    ball.update_position()
    assert ball.vel[1] == -3


@pytest.mark.unit
def test_ball_bounce_horizontal_wall(ball: Ball) -> None:
    ball.pos = [620, 460]  # Near the bottom-right corner
    ball.update_position()
    assert ball.vel[0] == -5
