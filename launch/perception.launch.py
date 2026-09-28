from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    perception_config = LaunchConfiguration('perception_config')

    declare_perception_config = DeclareLaunchArgument(
        'perception_config',
        default_value=PathJoinSubstitution([FindPackageShare('turtlebot_capabilities'), 'config', 'perception_config.yaml']),
        description='Absolute path to the TurtleBot perception configuration file'
    )

    perception_server = Node(
        package='fp_perception',
        executable='fp_perception_node',
        name='perception_node',
        parameters=[perception_config],
        output='screen',
        arguments=['--ros-args', '--log-level', 'info']
    )
    
    return LaunchDescription([
        declare_perception_config,
        perception_server,
    ])

