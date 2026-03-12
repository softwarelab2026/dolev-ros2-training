import pytest
from ball_tracking_system.logic.ball import Ball

@pytest.mark.unit
def test_when_ball_movement(
) -> None:
    vel_x = 5
    vel_y = 3
    ball = Ball(width=640, height=480, ball_radius=20, ball_vel_x=vel_x, ball_vel_y=vel_y)
    x_before, y_before = ball.ball_pos 
    ball.move_objects()
    x_after, y_after = ball.ball_pos

    assert x_before + 5 == x_after
    assert y_before + 3 == y_after
    
    

@pytest.mark.unit
def test_ball_bounce_vertical_wall() -> None:
    ball = Ball(width=200, height=200, ball_radius=20, ball_vel_x=40, ball_vel_y=2)

    ball.move_objects()
    ball.move_objects()
    ball.move_objects()

    assert ball.ball_pos[0] == 140



@pytest.mark.unit
def test_ball_bounce_horizontal_wall(ball: Ball) -> None:
    ball.ball_pos = [300, 480]
    ball.move_objects()
    assert ball.ball_pos[1] == 477

    
    

