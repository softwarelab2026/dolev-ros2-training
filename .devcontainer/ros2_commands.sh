echo "export DISPLAY=host.docker.internal:0.0" >> /etc/bash.bashrc 
cd ros2_ws
echo "source /opt/ros/humble/setup.bash" >> /etc/bash.bashrc
colcon build --symlink-install
echo 'source /workspaces/dolev-ros2-training/ros2_ws/install/setup.bash' >> ~/.bashrc
