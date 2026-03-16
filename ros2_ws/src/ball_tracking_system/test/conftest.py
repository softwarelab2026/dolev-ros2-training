from ball_tracking_system.logic.ball import Ball
from ball_tracking_system.logic.frame_generator import generate_frame
import pytest
from ball_tracking_system.logic.pid_controller import PID
import numpy as np


@pytest.fixture  # type: ignore[misc]
def lower_red() -> np.ndarray:
    return np.array([0, 120, 70])


@pytest.fixture  # type: ignore[misc]
def upper_red() -> np.ndarray:
    return np.array([10, 255, 255])


@pytest.fixture  # type: ignore[misc]
def ball() -> Ball:
    return Ball(width=640, height=480, radius=20, vel_x=5, vel_y=3)


@pytest.fixture  # type: ignore[misc]
def frame() -> np.ndarray:
    return generate_frame(640, 480, [320, 240], 20)


@pytest.fixture  # type: ignore[misc]
def frame_without_ball() -> np.ndarray:
    return np.ones((640, 480, 3), dtype=np.uint8) * 255


@pytest.fixture  # type: ignore[misc]
def simple_pid() -> PID:
    return PID(1, 0, 0)
