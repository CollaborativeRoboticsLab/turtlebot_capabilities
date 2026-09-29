FROM ros:humble

# Add vscode user with same UID and GID as your host system
# (modified from https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user#_creating-a-nonroot-user)
# ubuntu now has a 1000 user ubuntu
ARG USERNAME=ubuntu
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

RUN apt-get update && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install --no-install-recommends -y \
    sudo \
    git \
    curl \
    libcurl4-openssl-dev \
    libpoco-dev \
    nlohmann-json3-dev \
    ros-${ROS_DISTRO}-navigation2 \
    ros-${ROS_DISTRO}-nav2-bringup` \
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
    libportaudio2 \
    portaudio19-dev \
    python3-pyaudio \
    alsa-utils \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Switch from root to user
USER $USERNAME

# Rosdep update
RUN rosdep update

# Source the ROS setup file
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc

## Install turtlebot4 dependencies
WORKDIR /home/$USERNAME/colcon_ws/src

RUN git clone https://github.com/turtlebot/turtlebot4_desktop.git -b humble
RUN git clone https://github.com/turtlebot/turtlebot4.git -b humble 

WORKDIR /home/$USERNAME/colcon_ws

RUN rosdep install --from-paths src --ignore-src -r -y

## Install capabilities and related packages
WORKDIR /home/$USERNAME/colcon_ws/src

RUN git clone https://github.com/CollaborativeRoboticsLab/capabilities2.git -b experience-integration
RUN git clone https://github.com/CollaborativeRoboticsLab/fabric.git -b experience-integration
RUN git clone https://github.com/CollaborativeRoboticsLab/fabric_capabilities.git -b experience-integration
RUN git clone --recurse-submodules https://github.com/CollaborativeRoboticsLab/prompt_tools.git -b experience-integration
RUN git clone https://github.com/CollaborativeRoboticsLab/prompt_capabilities.git -b experience-integration
RUN git clone https://github.com/CollaborativeRoboticsLab/fp_perception.git -b experience-integration
RUN git clone https://github.com/CollaborativeRoboticsLab/fp_perception_capabilities.git -b experience-integration
RUN git clone https://github.com/CollaborativeRoboticsLab/nav2_capabilities.git -b experience-integration
# git clone https://github.com/CollaborativeRoboticsLab/supervisor.git
# git clone https://github.com/CollaborativeRoboticsLab/experience.git
# git clone https://github.com/CollaborativeRoboticsLab/fabric_generator_experience.git
# git clone https://github.com/CollaborativeRoboticsLab/fabric_generator_prompttools.git