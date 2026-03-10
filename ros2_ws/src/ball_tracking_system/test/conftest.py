from ball_tracking_system.logic.ball import Ball
from ball_tracking_system.logic.frame_generator import Frame

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
    return Ball(x=100, y=100, radius=20, vx=5, vy=3)


@pytest.fixture
def frame():
    return Frame(width=640, height=480)
