#!/bin/bash

colcon build --symlink-install
source install/setup.bash
ros2 launch launch/ball_tracking_system_launch.py
