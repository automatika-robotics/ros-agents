FROM ubuntu:22.04 AS aggregator

# setup environment
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV ROS_DISTRO iron
ENV ROS_AUTOMATIC_DISCOVERY_RANGE SUBNET
ENV RMW_IMPLEMENTATION rmw_fastrtps_cpp
ENV AMENT_PREFIX_PATH /opt/ros/$ROS_DISTRO

RUN apt update && apt install -y apt-utils && apt install -y locales && echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN locale-gen en_US en_US.UTF-8 && update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

RUN apt install -y software-properties-common && add-apt-repository -y universe && apt install -y curl

RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null

RUN apt update && apt upgrade -y && apt install -y ros-iron-ros-base

RUN apt install -y ros-dev-tools && apt install -y ros-iron-rmw-fastrtps-cpp

RUN apt install -y python3-pip && apt clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pillow numpy opencv-python-headless redis[hiredis] msgpack

COPY aggregator_ROS /automatika/src/comp_serv

WORKDIR /automatika

RUN colcon build --packages-select comp_serv

COPY docker_entrypoints/start_server.sh .

RUN ["chmod", "+x", "/automatika/start_server.sh"]

FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04 as model_server

WORKDIR /automatika

COPY robo-ml /automatika/RoboML

RUN apt-get update && apt-get install -y python3 python3-pip && pip install pip-tools && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install -e RoboML/
