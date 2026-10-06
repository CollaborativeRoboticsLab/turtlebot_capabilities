from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    plan_file_name = LaunchConfiguration('filename')
    fabric_config = LaunchConfiguration('fabric_config')
    start_experience_stack = LaunchConfiguration('start_experience_stack')
    experience_only = LaunchConfiguration('experience_only')
    start_prompt_tools = LaunchConfiguration('start_prompt_tools')

    declare_plan_file_name = DeclareLaunchArgument(
        'filename',
        default_value='turtlebot_1.xml',
        description='Name of the plan file in turtlebot_capabilities/plans'
    )

    declare_fabric_config = DeclareLaunchArgument(
        'fabric_config',
        default_value=PathJoinSubstitution([FindPackageShare('fabric_server'), 'config', 'fabric.yaml']),
        description='Absolute path to the fabric configuration file'
    )

    declare_start_experience_stack = DeclareLaunchArgument(
        'start_experience_stack',
        default_value='true',
        description='Whether to start the experience and supervisor stack alongside fabric'
    )

    declare_experience_only = DeclareLaunchArgument(
        'experience_only',
        default_value='false',
        description='Whether to rebuild CoreGraphRag through the Experience stack without starting fabric'
    )

    declare_start_prompt_tools = DeclareLaunchArgument(
        'start_prompt_tools',
        default_value='true',
        description='Whether to start prompt_bridge for prompt-based plan generation; set false to disable it'
    )

    plan_file_path = PathJoinSubstitution([FindPackageShare('turtlebot_capabilities'), 'plans', plan_file_name])
    fabric_launch_path = PathJoinSubstitution([FindPackageShare('fabric_server'), 'launch', 'fabric.launch.py'])

    fabric = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(fabric_launch_path),
        launch_arguments={
            'plan_file_path': plan_file_path,
            'fabric_config': fabric_config,
            'start_experience_stack': start_experience_stack,
            'experience_only': experience_only,
            'start_prompt_tools': start_prompt_tools,
        }.items(),
    )

    return LaunchDescription([
        declare_plan_file_name,
        declare_fabric_config,
        declare_start_experience_stack,
        declare_experience_only,
        declare_start_prompt_tools,
        fabric
    ])

