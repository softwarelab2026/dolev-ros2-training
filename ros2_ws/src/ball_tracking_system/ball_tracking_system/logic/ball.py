class Ball:
    def __init__(self, width, height, radius, vel_x, vel_y):
        self._width = width

        self._height = height
        self.radius = radius
        self.pos = [width // 2, height // 2]

        self.vel = [vel_x, vel_y]

    def move_objects(self):
        if self.pos[0] <= self.radius or self.pos[0] >= self._width - self.radius:
            self.vel[0] = -self.vel[0]

        if self.pos[1] <= self.radius or self.pos[1] >= self._height - self.radius:
            self.vel[1] = -self.vel[1]

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
