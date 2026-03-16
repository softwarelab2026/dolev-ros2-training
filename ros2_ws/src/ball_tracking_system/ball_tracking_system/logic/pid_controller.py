import time


class PID:
    def __init__(self, kp, ki, kd):
        self._kp = kp
        self._ki = ki
        self._kd = kd
        self._prev_error = 0
        self._integral = 0

    def compute(self, error, dt):
        self._integral += error * dt

        if dt > 0:
            derivative = (error - self._prev_error) / dt
        else:
            derivative = 0

        output = self._kp * error + self._ki * self._integral + self._kd * derivative

        self._prev_error = error

        return output
