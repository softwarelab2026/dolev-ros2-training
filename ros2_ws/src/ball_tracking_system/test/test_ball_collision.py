import pytest
from ball_tracking_system.logic.ball import Ball


@pytest.mark.unit
def test_when_ball_movement() -> None:
    vel_x = 5
    vel_y = 3
    ball = Ball(width=640, height=480, radius=20, vel_x=vel_x, vel_y=vel_y)
    
    ball.move_objects()
    

    assert ball.pos[0] == 325
    assert ball.pos[1] == 243


@pytest.mark.unit
def test_ball_bounce_vertical_wall() -> None:
    ball = Ball(width=200, height=200, radius=20, vel_x=40, vel_y=2)
    ball.move_objects()
    ball.move_objects()
    ball.move_objects()

    assert ball.pos[0] == 140


@pytest.mark.unit
def test_ball_bounce_horizontal_wall(ball: Ball) -> None:
    ball = Ball(width=200, height=200, radius=20, vel_x=40, vel_y=120)
    ball.move_objects()
    
    

    assert ball.pos[1] == 140