from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Publisher Node
        Node(
            package='mypkg',  # パッケージ名
            executable='publisher',  # setup.py で定義したエントリポイント
            name='publisher',  # ノード名
        ),
        # Subscriber Node
        Node(
            package='mypkg',  # パッケージ名
            executable='subscriber',  # setup.py で定義したエントリポイント
            name='subscriber',  # ノード名
            output='screen',  # 出力をターミナルに表示
        ),
    ])

