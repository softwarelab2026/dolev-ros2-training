import numpy as np
import cv2
from ball_tracking_system.logic.ball import Ball


class Frame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = np.ones((height, width, 3), dtype=np.uint8) * 255

    def draw(self, ball: Ball):
        cv2.circle(
            self.data,
            (int(ball.pos[0]), int(ball.pos[1])),
            ball.radius,
            (0, 0, 255),
            -1,
        )
