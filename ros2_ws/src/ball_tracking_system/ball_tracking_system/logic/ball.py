class Ball:
    def __init__(
        self,
        x: float = 100,
        y: float = 100,
        radius: float = 20,
        vx: float = 5,
        vy: float = 3,
    ) -> None:
        self.pos = [x, y]
        self.vel = [vx, vy]
        self.radius = radius

    def set_position(self, x: float, y: float) -> None:
        self.pos[0] = x
        self.pos[1] = y

    def move_by_velocity(self) -> None:
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def update_position(self, width, height) -> None:
        self.move_by_velocity()

        if self._does_bounce_horizontal(width):
            self.vel[0] *= -1
        if self._does_bounce_vertical(height):
            self.vel[1] *= -1

    def _does_bounce_horizontal(self, width) -> bool:
        return self.pos[0] - self.radius <= 0 or self.pos[0] + self.radius >= width

    def _does_bounce_vertical(self, height) -> bool:
        return self.pos[1] - self.radius <= 0 or self.pos[1] + self.radius >= height
