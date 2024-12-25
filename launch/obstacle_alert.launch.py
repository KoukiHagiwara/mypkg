from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mypkg',
            executable='publisher',
            name='publisher',
        ),
        Node(
            package='mypkg',
            executable='subscriber',
            name='subscriber',
        ),
    ])

