from ball_tracking_system.logic.frame_generator import FrameGenerator

import pytest

import numpy as np


@pytest.fixture
def lower_red():
    return np.array([0, 120, 70])


@pytest.fixture
def upper_red():
    return np.array([10, 255, 255])


@pytest.fixture
def frame_generator():
    return FrameGenerator(width=640, height=480, ball_radius=20)
