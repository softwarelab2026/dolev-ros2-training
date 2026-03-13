FROM osrf/ros:humble-desktop

WORKDIR /ros2_ws

COPY ../ros2_ws/ ./  

COPY ./ros2_ws/run.sh /ros2_ws/run.sh

RUN chmod +x /ros2_ws/run.sh

RUN apt update && apt install -y \
    python3-pip \
    wget \
    x11-apps \
    libxcb-xinerama0 \
    ros-humble-turtlesim \
    ros-humble-rqt \
    ros-humble-rqt-common-plugins \
    ros-humble-cv-bridge \
    python3-colcon-core \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
RUN pip3 install pre-commit pytest

RUN echo "source /opt/ros/humble/setup.bash" >> /etc/bash.bashrc

ENV DISPLAY=host.docker.internal:0


CMD ["/ros2_ws/run.sh"]