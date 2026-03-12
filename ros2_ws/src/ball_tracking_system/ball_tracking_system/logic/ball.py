

class Ball:
    
    def __init__(self, width, height, ball_radius, ball_vel_x, ball_vel_y):
        self._width = width
    
        self._height = height
        self.ball_radius = ball_radius

        self.ball_pos = [width // 2, height // 2]
        self._ball_vel = [ball_vel_x, ball_vel_y]

    
    def move_objects(self):
        if (
            self.ball_pos[0] <= self.ball_radius
            or self.ball_pos[0] >= self._width - self.ball_radius
        ):
            self._ball_vel[0] = -self._ball_vel[0]

        if (
            self.ball_pos[1] <= self.ball_radius
            or self.ball_pos[1] >= self._height - self.ball_radius
        ):
            self._ball_vel[1] = -self._ball_vel[1]

        self.ball_pos[0] += self._ball_vel[0]
        self.ball_pos[1] += self._ball_vel[1]


