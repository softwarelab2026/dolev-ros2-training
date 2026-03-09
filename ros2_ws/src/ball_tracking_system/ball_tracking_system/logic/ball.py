class Ball:
    def __init__(
        self,
        x: int = 100,
        y: int = 100,
        radius: int = 20,
        vx: int = 5,
        vy: int = 3,
        width: int = 640,
        height: int = 480,
    ) -> None:
        self.pos = [x, y]
        self.vel = [vx, vy]
        self.radius = radius
        self.width = width
        self.height = height

    def update_position(self) -> None:
        self._move_ball()

        if self._does_bounce_horizontal():
            self.vel[0] *= -1
        if self._does_bounce_vertical():
            self.vel[1] *= -1

    def _does_bounce_horizontal(self) -> bool:
        return self.pos[0] - self.radius <= 0 or self.pos[0] + self.radius >= self.width

    def _does_bounce_vertical(self) -> bool:
        return (
            self.pos[1] - self.radius <= 0 or self.pos[1] + self.radius >= self.height
        )

    def _move_ball(self) -> None:
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
