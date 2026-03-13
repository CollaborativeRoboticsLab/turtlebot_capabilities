# Turtlebot Capabilities

Provides capabiilites2 runners for Turtlebot robots

## Examples

Examples depend on [CollaborativeRoboticsLab/capabilities2](https://github.com/CollaborativeRoboticsLab/capabilities2), [CollaborativeRoboticsLab/perception](https://github.com/CollaborativeRoboticsLab/perception) and [CollaborativeRoboticsLab/prompt_tools](https://github.com/CollaborativeRoboticsLab/prompt_tools).

| Example | Description |
| ---     | ---         |
| [turtlebot_1.xml](./plans/turtlebot_1.xml) | In this example The LLM would need to generate a plan that moves the robot 1 meter forward, turn left and take a picture. And then try to describe what it sees. |
| [turtlebot_2.xml](./plans/turtlebot_2.xml) | In this example, we define two points as point A and B as world information. The LLM would need to generate a plan or more that moves the robot To the point A and check for a person using vision or audio, then ask for the name. Then it should come back to the origin and repeat the name. | 
| [turtlebot_3.xml](./plans/turtlebot_3.xml) | In this example, we define two points as point A and B as world information. The LLM would need to generate a plan or more that moves the robot To the point A and check for a person using vision or audio, then ask for the name. Then it should come back to the origin and repeat the name. If the person is not there, the robot is supposed to Go to point B instead. | 

## Run

To run the examples, first make sure that the robot is running and then on seperate terminals run,

```bash
source install/setup.bash
ros2 launch capabilities2_server capabilities2_server.launch.py
```

```bash
export OPENAI_API_KEY=
source install/setup.bash
ros2 launch perception server.launch.py
```

```bash
export OPENAI_API_KEY=
source install/setup.bash
ros2 launch prompt_bridge prompt_bridge.launch.py
```

```bash
source install/setup.bash
ros2 launch turtlebot_capabilities system.launch.py filename:=turtlebot_1.xml
```

Change `filename:=turtlebot_1.xml` to match the correct plan