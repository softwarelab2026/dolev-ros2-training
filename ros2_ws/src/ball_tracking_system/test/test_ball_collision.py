import pytest
from ball_tracking_system.logic.frame_generator import FrameGenerator

@pytest.mark.unit
def test_when_ball_movement(
    frame_generator: FrameGenerator, lower_red, upper_red
) -> None:
    
    # width=640, height=480
    x_before, y_before = frame_generator.ball_pos 
    frame_generator.move_objects()
    x_after, y_after = frame_generator.ball_pos

    assert x_before + frame_generator.ball_vel[0] == x_after
    assert y_before +frame_generator.ball_vel[1] == y_after
    
    

@pytest.mark.unit
def test_ball_bounce_vertical_wall(frame_generator: FrameGenerator, lower_red, upper_red) -> None:
    frame_generator.ball_pos = [640, 460]  # Near the right wall 
    frame_generator.move_objects()
    assert frame_generator.ball_pos[0] == 635


@pytest.mark.unit
def test_ball_bounce_horizontal_wall(frame_generator: FrameGenerator, lower_red, upper_red) -> None:
    frame_generator.ball_pos = [300, 480]
    frame_generator.move_objects()
    assert frame_generator.ball_pos[1] == 477

    
    

