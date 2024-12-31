# SPDX-FileCopyrightText: 2024 Kouki Hagiwara
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import random

class obstacle_alert(Node):
    def __init__(self):
        super().__init__("obstacle_alert")
        self.publisher_ = self.create_publisher(LaserScan, "scan", 10)
        self.timer = self.create_timer(1.0, self.publish_scan_data)
        self.threshold_distance = 0.5

    def publish_scan_data(self):
        msg = LaserScan()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'laser_frame'

        # スキャンデータの生成
        ranges = [random.uniform(0.1, 2.0) for _ in range(360)]
        msg.ranges = ranges

        # 障害物検知処理
        min_distance = min(ranges)
        if min_distance < self.threshold_distance:
            # トピックに警告情報を含める
            msg.header.frame_id = f'laser_frame_WARNING_obstacle_{min_distance:.2f}m'
            # 開発用のログ出力
            self.get_logger().info(f'Warning: Obstacle detected at {min_distance:.2f}m')
        else:
            # 通常のログ出力
            self.get_logger().info(f'Current minimum distance: {min_distance:.2f}m')

        msg.angle_min = -3.14
        msg.angle_max = 3.14
        msg.angle_increment = 3.14 / 180
        msg.range_min = 0.1
        msg.range_max = 2.0

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = obstacle_alert()
    rclpy.spin(node)
