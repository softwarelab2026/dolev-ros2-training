# Ball Tracking System

## Launching the Ball Tracking System

To launch the ball tracking system:

```bash
cd ros_ws
colcon build --symlink-install
source install/setup.bash
ros2 launch launch/ball_tracking_system_launch.py
```
if you want to achive the same resault but with ton of terminals:
```bash 

ros2 run ball_tracking_system camera_node
ros2 run ball_tracking_system ball_detector_node 
ros2 run ball_tracking_system control_robot_node 
ros2 run rqt_gui rqt_gui
ros2 run turtlesim turtlesim_node

```


## Running Tests

To run tests you can use tasks:

```bash
cd ros2_ws/src/ball_tracking_system/ball_tracking_system
python3 -m pytest -m unit
```

Or just use the `tasks.json` (like a normal human being).
