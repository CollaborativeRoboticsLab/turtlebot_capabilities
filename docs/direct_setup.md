# Direct Installation

## Dependencies

Follow these setups only if you are **not** using a devcontainer. Install the following dependencies in your workspace to run the examples.

```bash
sudo apt update
sudo apt install -y git \
    curl \
    libcurl4-openssl-dev \
    libpoco-dev \
    nlohmann-json3-dev \
    ros-${ROS_DISTRO}-navigation2 \
    ros-${ROS_DISTRO}-nav2-bringup \
    ros-${ROS_DISTRO}-slam-toolbox \
    ros-${ROS_DISTRO}-rqt-robot-monitor \
    ros-${ROS_DISTRO}-irobot-create-msgs \
    ros-${ROS_DISTRO}-irobot-create-description \
    ros-${ROS_DISTRO}-joint-state-publisher \
    ros-${ROS_DISTRO}-rmw-fastrtps-cpp \
    ros-${ROS_DISTRO}-vision-opencv \
    ros-${ROS_DISTRO}-cv-bridge \
    ros-${ROS_DISTRO}-image-transport \
    ros-${ROS_DISTRO}-bondcpp \
    ros-${ROS_DISTRO}-rviz2 \
    ros-${ROS_DISTRO}-teleop-twist-keyboard \
    ros-${ROS_DISTRO}-ros-gz \
    ros-${ROS_DISTRO}-gz-ros2-control \
    libportaudio2 \
    portaudio19-dev \
    python3-pyaudio \
    alsa-utils \
    iputils-ping \
```

## Core packages

Follow these setups only if you are **not** using a devcontainer. Above examples depend on the capabilities2, fp_perception, prompt_tools, fabric and turtlebot_capabilities packages. You can clone these packages in your workspace and build them using colcon build.

```bash
cd ~/colcon_ws/src
git clone https://github.com/turtlebot/turtlebot4_desktop.git -b jazzy
git clone https://github.com/turtlebot/turtlebot4.git -b jazzy

cd ~/colcon_ws
rosdep install --from-paths src --ignore-src -r -y

cd ~/colcon_ws/src
git clone https://github.com/CollaborativeRoboticsLab/capabilities2.git -b develop
git clone https://github.com/CollaborativeRoboticsLab/fabric.git
git clone https://github.com/CollaborativeRoboticsLab/fabric_capabilities.git
git clone https://github.com/CollaborativeRoboticsLab/prompt_tools.git
git clone https://github.com/CollaborativeRoboticsLab/prompt_capabilities.git
git clone https://github.com/CollaborativeRoboticsLab/fp_perception.git
git clone https://github.com/CollaborativeRoboticsLab/fp_perception_capabilities.git
git clone https://github.com/CollaborativeRoboticsLab/nav2_capabilities.git
git clone https://github.com/CollaborativeRoboticsLab/turtlebot_capabilities.git
git clone https://github.com/CollaborativeRoboticsLab/turtlebot4_simulations.git

cd ~/colcon_ws
colcon build --symlink-install
```