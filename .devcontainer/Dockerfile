# Start from ROS2 Humble desktop
FROM osrf/ros:humble-desktop

RUN apt update && apt install -y \
    python3-pip \
    wget \
    x11-apps \
    libxcb-xinerama0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
RUN pip3 install pre-commit pytest

RUN apt update



RUN apt update && apt install -y --no-install-recommends \
    ros-humble-turtlesim \
    ros-humble-rqt \
    ros-humble-rqt-common-plugins \
    ros-humble-cv-bridge \
    python3-colcon-core \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

RUN echo "source /opt/ros/humble/setup.bash" >> /etc/bash.bashrc

CMD ["bash"]