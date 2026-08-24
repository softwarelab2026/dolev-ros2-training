class PID:
    def __init__(self, kp: float, ki: float, kd: float) -> None:
        self._kp = kp
        self._ki = ki
        self._kd = kd
        self._prev_error = 0.0
        self._integral = 0.0

    def compute(self, error: float, dt: float) -> float:
        self._integral += error * dt

        if dt > 0:
            derivative = (error - self._prev_error) / dt
        else:
            derivative = 0

        output = self._kp * error + self._ki * self._integral + self._kd * derivative

        self._prev_error = error

        return output
