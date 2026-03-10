# Start from ROS2 Humble desktop
FROM osrf/ros:humble-desktop

COPY requirements.txt .

RUN apt update
# Install pip
RUN apt install -y python3-pip
RUN apt install -y wget
RUN pip3 install --upgrade pip
RUN pip3 install pre-commit pytest

# Install python dependencies
RUN apt install -y ros-humble-turtlesim ros-humble-rqt ros-humble-cv-bridge python3-colcon-core python3-colcon-common-extensions


RUN echo "source /opt/ros/humble/setup.bash" >> /etc/bash.bashrc
