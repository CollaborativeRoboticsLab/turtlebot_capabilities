# Turtlebot Capabilities

Provides execution plans for Turtlebot robots. These has been tested with a Turtlebot4 robot. 

## Examples

Examples depend on [CollaborativeRoboticsLab/capabilities2](https://github.com/CollaborativeRoboticsLab/capabilities2), [CollaborativeRoboticsLab/fp_perception](https://github.com/CollaborativeRoboticsLab/fp_perception), [CollaborativeRoboticsLab/prompt_tools](https://github.com/CollaborativeRoboticsLab/prompt_tools) and [CollaborativeRoboticsLab/fabric](https://github.com/CollaborativeRoboticsLab/fabric).

Modify the following example plans to work with your robot and environment. These plans are designed to work with our lab's setup and might need modifications to work with your robot or environment.


| Example | Description |
| ---     | ---         |
| [turtlebot_1.xml](./plans/turtlebot_1.xml) | Moves the robot to the waypoint at (-2.5, 2.0). |
| [turtlebot_2.xml](./plans/turtlebot_2.xml) | Moves the robot through five waypoints: (0.5, 2.0), (1.0, 2.0), (2.0, 0.5), (2.0, -1.0), and (-2.0, 0.0). |
| [turtlebot_3.xml](./plans/turtlebot_3.xml) | Moves through several waypoints and defines a recovery branch that returns to (0.0, 0.5) if the (2.0, -3.0) waypoint fails. |
| [turtlebot_4.xml](./plans/turtlebot_4.xml) | Moves through multiple waypoints with recovery branches attached after several steps, including a recovery path through (0.0, -3.0) and back to (0.0, 0.5) if the (2.0, -3.0) step fails. |
| [turtlebot_5.xml](./plans/turtlebot_5.xml) | Prompts the LLM to generate a plan that moves the robot one meter forward and then describe what it sees in speech. |
| [turtlebot_6.xml](./plans/turtlebot_6.xml) | Provides world information for points A and B, then prompts the LLM to generate a plan that goes to point A, asks for a person's name, returns to the origin, and repeats the name. | 
| [turtlebot_7.xml](./plans/turtlebot_7.xml) | Provides world information for points A and B, then prompts the LLM to generate a plan that goes to point A, asks for a person's name if someone is there, returns to the origin to repeat it, and otherwise moves to point B. | 
| [turtlebot_7a.xml](./plans/turtlebot_7a.xml) | Same as task 7 but use vision to detect the person. |


## Setup

We recommend using a devcontainer to run the examples. You can modify the provided [Humble devcontainer config](./.devcontainer/humble/devcontainer.json) or [Jazzy devcontainer config](./.devcontainer/jazzy/devcontainer.json) to easily connect with your turtlebot4 by updating the following specific configuration. We use the "FASTRTPS" middleware on the Turtlebot4. The devcontainers are configured to work with ROS2 Humble and Jazzy.

```json
"containerEnv": {
  "ROS_DOMAIN_ID": "10",
  "RMW_IMPLEMENTATION": "rmw_fastrtps_cpp",
  "ROS_DISCOVERY_SERVER": "10.0.0.192:11811"
}
```

`ROS_DOMAIN_ID` and `ROS_DISCOVERY_SERVER` should be updated to match your robot's configuration. You can find the robot's configuration by running the following command on the robot's terminal,

```bash
echo $ROS_DOMAIN_ID
echo $ROS_DISCOVERY_SERVER
```

> If you are not using a devcontainer, follow the [instructions here](./docs/direct_setup.md).

## Run

### Mapping the environment

Turtlebot4 can be used without mapping the environment, but online SLAM can be computationally intensive, so it is recommended to map the environment first. 

Run the slam node on the robot after ssh into the robot and run the following command on the robot's terminal,

```bash
source install/setup.bash
ros2 launch turtlebot4_navigation slam.launch.py
```

On the remote computer, run the following command to visualize the map in rviz,

```bash
source install/setup.bash
ros2 launch turtlebot4_viz view_navigation.launch.py
```

If you need to use teleop twist keyboard, use the following command on the remote computer's terminal,

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p stamped:=true
```

Use the teleop node or provided Joystick to move the robot around and map the environment. Once you have mapped the environment, save the map using the slamtoolbox rviz interface on the remote computer. You can also save the map using the following command on the robot's terminal,

```bash
ros2 run nav2_map_server map_saver_cli -f <map_name> --ros-args -p map_subscribe_transient_local:=true
```
as an example, to save the map as obs_lab, run the following command on the robot's terminal,
```bash
ros2 run nav2_map_server map_saver_cli -f ~/obs_lab --ros-args -p map_subscribe_transient_local:=true
```

### Using the robot and nav2 stack

To run the examples, first make sure that the robot is started and start nav2 stack on the robot using the following commands on separate terminals on the robot,

#### Use the prior map, run the following command on the robot's terminal,

```bash
ros2 launch turtlebot4_navigation localization.launch.py map:=cr_lab.yaml
```

### Visualize the robot in rviz, and set the initial pose,

```bash
source install/setup.bash
ros2 launch turtlebot4_viz view_navigation.launch.py
```

### Starting the nav2 stack

Make sure to set the initial pose of the robot in rviz before starting the nav2 stack. Otherwise nav2 stack will not start properly. Once the initial pose is set, run the following command on the host computers terminal to start the nav2 stack,

```bash
ros2 launch turtlebot4_navigation nav2.launch.py
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
ros2 launch turtlebot_capabilities perception.launch.py
```

```bash
source install/setup.bash
ros2 launch turtlebot_capabilities system.launch.py filename:=turtlebot_1.xml start_experience_stack:=true
```

Change `filename:=turtlebot_1.xml` to match the correct plan

## Using Gazebo Harmonic Simulations

Multiple simulation scenarios are maintained in the separate `turtlebot4_simulations` repository. From the root of a ROS 2 workspace containing both repositories, build both packages and source the workspace:

Start the standard TurtleBot4 in the maze:

```bash
source install/setup.bash
ros2 launch turtlebot4_maze_sim turtlebot4_maze.launch.py
```

