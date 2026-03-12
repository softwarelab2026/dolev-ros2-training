import numpy as np
import cv2


class FrameGenerator:
    def __init__(self, width, height, ball_radius, ball_vel_x, ball_vel_y):
        self._width = width
    
        self._height = height
        self._ball_radius = ball_radius

        self.ball_pos = [width // 2, height // 2]
        self.ball_vel = [ball_vel_x, ball_vel_y]

        self.data = np.ones((height, width, 3), dtype=np.uint8) * 255
    
    def move_objects(self):
        self._move_ball()

    def _move_ball(self):
        if (
            self.ball_pos[0] <= self._ball_radius
            or self.ball_pos[0] >= self._width - self._ball_radius
        ):
            self.ball_vel[0] = -self.ball_vel[0]

        if (
            self.ball_pos[1] <= self._ball_radius
            or self.ball_pos[1] >= self._height - self._ball_radius
        ):
            self.ball_vel[1] = -self.ball_vel[1]

        self.ball_pos[0] += self.ball_vel[0]
        self.ball_pos[1] += self.ball_vel[1]

       

    def generate_frame(self):
        self.data = np.ones((self._height, self._width, 3), dtype=np.uint8) * 255
        cv2.circle(
            self.data,
            (int(self.ball_pos[0]), int(self.ball_pos[1])),
            self._ball_radius,
            (0, 0, 255),
            -1,
        )
