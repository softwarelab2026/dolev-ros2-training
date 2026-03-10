import numpy as np
import cv2


class Frame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = np.ones((height, width, 3), dtype=np.uint8) * 255

    def draw_ball(self, ball):
        cv2.circle(
            self.data,
            (int(ball.pos[0]), int(ball.pos[1])),
            ball.radius,
            (0, 0, 255),
            -1,
        )

    def update_position(self, ball) -> None:
        ball.move_ball()

        if self._does_bounce_horizontal(ball):
            ball.vel[0] *= -1
        if self._does_bounce_vertical(ball):
            ball.vel[1] *= -1

    def _does_bounce_horizontal(self, ball) -> bool:
        return ball.pos[0] - ball.radius <= 0 or ball.pos[0] + ball.radius >= self.width

    def _does_bounce_vertical(self, ball) -> bool:
        return (
            ball.pos[1] - ball.radius <= 0 or ball.pos[1] + ball.radius >= self.height
        )
