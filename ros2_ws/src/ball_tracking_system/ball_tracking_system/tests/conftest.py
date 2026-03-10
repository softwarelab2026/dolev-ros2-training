from ball_tracking_system.logic.ball import Ball
from ball_tracking_system.logic.frame import Frame

import pytest


@pytest.fixture
def ball():
    return Ball(x=100, y=100, radius=20, vx=5, vy=3)


@pytest.fixture
def frame():
    return Frame(width=640, height=480)
