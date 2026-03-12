import pytest
from ball_tracking_system.logic.frame_generator import FrameGenerator

@pytest.mark.unit
def test_when_ball_doesnt_collide(
    frame_generator: FrameGenerator, lower_red, upper_red
) -> None:
    
    # width=640, height=480

    frame_generator.move_objects()
    assert frame_generator.ball_vel[0] > 0
    assert frame_generator.ball_vel[1] > 0
    
    

    
    

