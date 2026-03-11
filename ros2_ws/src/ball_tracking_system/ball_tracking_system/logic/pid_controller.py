import time


class PID:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.prev_error = 0
        self.integral = 0
        self.prev_time = time.time()

    def compute(self, error):
        now = time.time()
        dt = now - self.prev_time

        self.prev_time = now

        self.integral += error * dt

        if dt > 0:
            derivative = (error - self.prev_error) / dt
        else:
            derivative = 0

        output = self.kp * error + self.ki * self.integral + self.kd * derivative

        self.prev_error = error

        return output
