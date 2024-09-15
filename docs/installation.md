# Installation 🛠️

## Pre-Requisits

### Install ROS

ROS Agents is built to be used with ROS2. All ROS distributions starting from _Iron_ are supported. Install ROS2 by following the instructions on the [official site](https://docs.ros.org/en/iron/Installation.html).

### Install a model serving platform

The core of ROS Agents is agnostic to model serving platforms. It currently supports [Ollama](https://ollama.com) and [RoboML](https://github.com/automatika-robotics/RoboML). Please install either of these by following the instructions provided by respective projects. Support for new platforms will be continuously added. If you would like to support a particular platform, please open an issue/PR.

```{tip}
For utilizing larger models, it is recommended that model serving platforms are not installed directly on the robot (or the edge device) but on a GPU powered machine on the local network (or one of the cloud providers).
```

## Install ROS Agents (Ubuntu)

**Binary packages for Ubuntu will be released soon. Check this space.**

## Install ROS Agents from source

Create your ROS workspace.
```shell
mkdir -p agents_ws/src
cd agents_ws/src
```
### Get Dependencies

Install python dependencies
```shell
pip install -U pillow numpy opencv-python-headless hiredis msgpack msgpack_numpy 'attrs>=23.2.0'
```

Download ROS Sugar.
```shell
git clone https://github.com/automatika-robotics/ros-sugar
```
### Install ROS Agents
```shell
git clone https://github.com/automatika-robotics/ros-agents.git
cd ..
colcon build
source install/setup.bash
python your_script.py
```
