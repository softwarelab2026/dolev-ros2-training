import math

class Ball:
    def __init__(self, width, height, radius, vel_x, vel_y):
        self._width = width

        self._height = height
        self.radius = radius
        self.pos = [width // 2, height // 2]

        self.vel = [vel_x, vel_y]

    def _move_axis(self, pos, vel, min_bound, max_bound):
        next_pos = pos + vel 
        if next_pos <= min_bound:
            overflow = min_bound - next_pos
            pos = min_bound + overflow
            vel = -vel
        elif next_pos >= max_bound:
            overflow = next_pos - max_bound
            pos = max_bound - overflow
            vel = -vel

        else:
            pos = next_pos

        return pos, vel
    def move_objects(self):

        self.pos[0], self.vel[0] = self._move_axis(
            self.pos[0],
            self.vel[0],
            self.radius,
            self._width - self.radius
        )

        self.pos[1], self.vel[1] = self._move_axis(
            self.pos[1],
            self.vel[1],
            self.radius,
            self._height - self.radius
        )