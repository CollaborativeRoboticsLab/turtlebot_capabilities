# Turtlebot Capabilities

Provides execution plans for Turtlebot robots. These has been tested with a Turtlebot4 robot. 

## Examples

Examples depend on [CollaborativeRoboticsLab/capabilities2](https://github.com/CollaborativeRoboticsLab/capabilities2), [CollaborativeRoboticsLab/perception](https://github.com/CollaborativeRoboticsLab/perception),  [CollaborativeRoboticsLab/prompt_tools](https://github.com/CollaborativeRoboticsLab/prompt_tools) and [CollaborativeRoboticsLab/fabric](https://github.com/CollaborativeRoboticsLab/fabric).

Modify the following example plans to work with your robot and environment. These plans are designed to work with our lab's setup and might need modifications to work with your robot or environment.


| Example | Description |
| ---     | ---         |
| [turtlebot_1.xml](./plans/turtlebot_1.xml) | In this example (0.5,2) point is reachable. And the robot moves to that point. |
| [turtlebot_2.xml](./plans/turtlebot_2.xml) | In this example, (0.5,2) (1,2) (2,0.5) (-2,0) points are reachable. And the robot moves through those points. |
| [turtlebot_3.xml](./plans/turtlebot_3.xml) | In this example, (0.5,2) (1,2) (-2,0) are reachable, (2,-3) point is not reachable. Because of this, the robot moves to the (0,0.5) as a recovery action. |
| [turtlebot_4.xml](./plans/turtlebot_4.xml) | In this example, (0.5,2) (1,2) (2,1) are reachable, (2,-3), (0, -3) points are not reachable.Because of this, the robot moves to the (0,0.5) as a recovery action. (1,2) (2,1) points also have recovery actions linked, but they are not triggered as the point is accessible. |
| [turtlebot_5.xml](./plans/turtlebot_5.xml) | In this example The LLM would need to generate a plan that moves the robot 1 meter forward, turn left and take a picture. And then try to describe what it sees. |
| [turtlebot_6.xml](./plans/turtlebot_6.xml) | In this example, we define two points as point A and B as world information. The LLM would need to generate a plan or more that moves the robot To the point A and check for a person using vision or audio, then ask for the name. Then it should come back to the origin and repeat the name. | 
| [turtlebot_7.xml](./plans/turtlebot_7.xml) | In this example, we define two points as point A and B as world information. The LLM would need to generate a plan or more that moves the robot To the point A and check for a person using vision or audio, then ask for the name. Then it should come back to the origin and repeat the name. If the person is not there, the robot is supposed to Go to point B instead. | 


## Setup

Above examples depend on the capabilities2, perception, prompt_tools and fabric packages. You can clone these packages in your workspace and build them using colcon build.

```bash
cd ~/colcon_ws/src
git clone https://github.com/CollaborativeRoboticsLab/capabilities2.git -b develop
git clone https://github.com/CollaborativeRoboticsLab/fabric.git
git clone https://github.com/CollaborativeRoboticsLab/fabric_capabilities.git
git clone https://github.com/CollaborativeRoboticsLab/prompt_tools.git
git clone https://github.com/CollaborativeRoboticsLab/prompt_capabilities.git
git clone https://github.com/CollaborativeRoboticsLab/perception.git
git clone https://github.com/CollaborativeRoboticsLab/perception_capabilities.git
git clone https://github.com/CollaborativeRoboticsLab/nav2_capabilities.git

cd ~/colcon_ws
colcon build --symlink-install
```

## Run

### Starting the robot and nav2 stack

To run the examples, first make sure that the robot is started and start nav2 stack on the robot using the following commands on separate terminals on the robot,

```bash
ros2 launch turtlebot4_navigation slam.launch.py
````

```bash
ros2 launch turtlebot4_navigation nav2.launch.py
```

Optional: If you want to visualize the robot in rviz, run the following command on remote computer's terminal,

```bash
ros2 launch turtlebot4_viz view_navigation.launch.py
```

> Note: Due to the interaction between CLI tools such as `ros2 topic ...`, `ros2 node ...` and rmw_fastrtps_cpp which we use in this devcontainer to communicate with the robot, it is recommended to use the `export ROS_SUPER_CLIENT=1` environment variable on the remote computer to avoid any issues with the CLI tools. Don't add the `export ROS_SUPER_CLIENT=1` to your bashrc, as it can cause issues with normal ROS2 nodes execution under rmw_fastrtps_cpp. Only use it when you are using CLI tools to communicate with the robot as shown below.

```bash
export ROS_SUPER_CLIENT=1
ros2 daemon stop && ros2 daemon start
ros2 topic list
```

### Starting the capabilities2 server and turtlebot capabilities

Then on remote computer to start the system, on seperate terminals run,

```bash
source install/setup.bash
ros2 launch capabilities2_server capabilities2_server.launch.py
```

```bash
export OPENAI_API_KEY=
source install/setup.bash
ros2 launch turtlebot_capabilities perception.launch.py
```

> Note, to accomodate the sensor setup/topics in the turtlebot4, we use a custom [perception config file](./config/perception_config.yaml) seperate from the default config found on the perception package. You can modify the config file to match your robot's sensor setup.

```bash
export OPENAI_API_KEY=
source install/setup.bash
ros2 launch prompt_bridge prompt_bridge.launch.py
```

```bash
source install/setup.bash
ros2 launch turtlebot_capabilities fabric.launch.py filename:=turtlebot_1.xml
```

Change `filename:=turtlebot_1.xml` to match the correct plan
