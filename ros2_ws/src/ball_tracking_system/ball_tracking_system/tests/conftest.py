from logic.ball import Ball
import pytest


@pytest.fixture
def ball():
    return Ball(x=100, y=100, radius=20, vx=5, vy=3, width=640, height=480)
