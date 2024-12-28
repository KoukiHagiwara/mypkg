# SPDX-FileCopyrightText: 2024 Kouki Hagiwara
# SPDX-License-Identifier: BSD-3-Clause

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Publisher Node
        Node(
            package='mypkg',  # パッケージ名
            executable='transmitter',  # setup.py で定義したエントリポイント
            name='transmitter',  # ノード名
        ),
        # Subscriber Node
        Node(
            package='mypkg',  # パッケージ名
            executable='detection',  # setup.py で定義したエントリポイント
            name='detection',  # ノード名
            output='screen',  # 出力をターミナルに表示
        ),
    ])

