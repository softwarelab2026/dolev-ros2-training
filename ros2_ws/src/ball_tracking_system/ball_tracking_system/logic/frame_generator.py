import numpy as np
import cv2


class FrameGenerator:
    def __init__(self, width, height, ball_radius):
        self.width = width
        self.height = height
        self.ball_radius = ball_radius

        self.ball_pos = [width // 2, height // 2]
        self.ball_val = [3, 2]

        self.data = np.ones((height, width, 3), dtype=np.uint8) * 255

    def move_objects(self):
        self._move_ball()

    def _move_ball(self):
        self.ball_pos[0] += self.ball_val[0]
        self.ball_pos[1] += self.ball_val[1]

        if (
            self.ball_pos[0] <= self.ball_radius
            or self.ball_pos[0] >= self.width - self.ball_radius
        ):
            self.ball_val[0] = -self.ball_val[0]

        if (
            self.ball_pos[1] <= self.ball_radius
            or self.ball_pos[1] >= self.height - self.ball_radius
        ):
            self.ball_val[1] = -self.ball_val[1]

    def generate_frame(self):
        self.data = np.ones((self.height, self.width, 3), dtype=np.uint8) * 255
        cv2.circle(
            self.data,
            (int(self.ball_pos[0]), int(self.ball_pos[1])),
            self.ball_radius,
            (0, 0, 255),
            -1,
        )
