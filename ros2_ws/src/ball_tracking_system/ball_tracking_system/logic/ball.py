class Ball:
    def __init__(
        self,
        x: int = 100,
        y: int = 100,
        radius: int = 20,
        vx: int = 5,
        vy: int = 3,
    ) -> None:
        self.pos = [x, y]
        self.vel = [vx, vy]
        self.radius = radius

    def move_ball(self) -> None:
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
