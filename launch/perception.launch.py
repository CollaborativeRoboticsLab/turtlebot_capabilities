from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PathJoinSubstitution
from launch.substitutions import PythonExpression
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    perception_config = LaunchConfiguration('perception_config')

    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use Gazebo time and the simulation perception configuration'
    )

    declare_namespace = DeclareLaunchArgument(
        'namespace',
        default_value='',
        description='ROS namespace matching the robot sensor bridge'
    )

    declare_perception_config = DeclareLaunchArgument(
        'perception_config',
        default_value=PathJoinSubstitution([
            FindPackageShare('turtlebot_capabilities'),
            'config',
            PythonExpression([
                "'perception_config_sim.yaml' if '", use_sim_time,
                "'.lower() in ('true', '1') else 'perception_config.yaml'"
            ])
        ]),
        description='Absolute path to the TurtleBot perception configuration file'
    )

    perception_server = Node(
        package='fp_perception',
        executable='fp_perception_node',
        name='perception_node',
        namespace=LaunchConfiguration('namespace'),
        parameters=[perception_config, {
            'use_sim_time': ParameterValue(use_sim_time, value_type=bool)
        }],
        output='screen',
        arguments=['--ros-args', '--log-level', 'info']
    )
    
    return LaunchDescription([
        declare_use_sim_time,
        declare_namespace,
        declare_perception_config,
        perception_server,
    ])

