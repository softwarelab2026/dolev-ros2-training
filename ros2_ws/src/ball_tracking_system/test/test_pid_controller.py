from ball_tracking_system.logic.pid_controller import PID

# im so excited to start my PID checking


def test_proportional_works() -> None:
    pid = PID(4, 0, 0)
    assert pid.compute(4, 1) == 16


def test_when_dt_changed_proportional_still_works_the_same() -> None:
    pid = PID(4, 0, 0)
    assert pid.compute(4, 1) == 16 and pid.compute(4, 100) == 16


def test_one_integrational_when_4_seconds_passed_compute_works() -> None:
    pid = PID(0, 1, 0)
    assert pid.compute(4, 4) == 16


def test_two_integrational_when_4_seconds_passed() -> None:
    pid = PID(0, 1, 0)
    pid.compute(4, 4)  # should return 16
    assert pid.compute(4, 4) == 32


def test_one_derivate_when_second_passed() -> None:
    pid = PID(0, 0, 1)
    assert pid.compute(4, 1) == 4


def test_one_derivative_when_4_seconds_passed() -> None:
    pid = PID(0, 0, 1)
    assert pid.compute(4, 4) == 1


def test_two_derivative_when_second_passed() -> None:
    pid = PID(0, 0, 1)
    pid.compute(error=4, dt=10)
    assert pid.compute(error=4, dt=7) == 0
