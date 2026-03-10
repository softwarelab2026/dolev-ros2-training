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
