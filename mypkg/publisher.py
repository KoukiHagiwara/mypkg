import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import random

class PublisherNode(Node):
    def __init__(self):
        super().__init__("publisher")
        self.publisher_ = self.create_publisher(LaserScan, "scan", 10)
        self.timer = self.create_timer(1.0, self.publish_scan_data)  # 毎秒1回

    def publish_scan_data(self):
        msg = LaserScan()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'laser_frame'

        # ダミーデータの生成 (0.1m 〜 2.0m の範囲で乱数)
        msg.ranges = [random.uniform(0.1, 2.0) for _ in range(360)]
        msg.angle_min = -3.14
        msg.angle_max = 3.14
        msg.angle_increment = 3.14 / 180
        msg.range_min = 0.1
        msg.range_max = 2.0

        self.publisher_.publish(msg)
        self.get_logger().info('Published scan data')

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)