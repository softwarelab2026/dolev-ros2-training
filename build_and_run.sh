#!/bin/bash
cd ros2_ws
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
ros2 launch launch/ball_tracking_system.launch.py
