from ball_tracking_system.logic.ball import Ball
from ball_tracking_system.logic.frame_generator import generate_frame
import pytest

import numpy as np


@pytest.fixture
def lower_red():
    return np.array([0, 120, 70])


@pytest.fixture
def upper_red():
    return np.array([10, 255, 255])


@pytest.fixture
def ball():
    return Ball(width=640, height=480, radius=20, vel_x=5, vel_y=3)


@pytest.fixture
def frame():
    return generate_frame(640, 480, [320, 240], 20)


@pytest.fixture
def frame_without_ball():
    return np.ones((640, 480, 3), dtype=np.uint8) * 255
