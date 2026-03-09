import cv2


class Ball:
    def __init__(self, x=100, y=100, radius=20, vx=5, vy=3, width=640, height=480):
        self.pos = [x, y]
        self.vel = [vx, vy]
        self.radius = radius
        self.width = width
        self.height = height

    def update_position(self):
        self._move_ball()

        if self._does_bounce_horizontal():
            self.vel[0] *= -1
        if self._does_bounce_vertical():
            self.vel[1] *= -1

    def _does_bounce_horizontal(self):
        return self.pos[0] - self.radius <= 0 or self.pos[0] + self.radius >= self.width

    def _does_bounce_vertical(self):
        return (
            self.pos[1] - self.radius <= 0 or self.pos[1] + self.radius >= self.height
        )

    def _move_ball(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def draw_on_frame(self, frame):
        cv2.circle(
            frame, (int(self.pos[0]), int(self.pos[1])), self.radius, (0, 0, 255), -1
        )
        return frame
