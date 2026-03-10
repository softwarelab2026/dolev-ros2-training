# Ball Tracking System

## Launching the Ball Tracking System

To launch the ball tracking system:

```bash
colcon build --symlink-install
source install/setup.bash
ros2 launch run.py
```
To observe the camera:
```bash 
ros2 run rqt_gui rqt_gui
```


## Running Tests

To run tests you can use tasks:

```bash
cd ros2_ws/src/ball_tracking_system/ball_tracking_system
python3 -m pytest -m unit
```

Or just use the `tasks.json` (like a normal human being).
