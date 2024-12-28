import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String


class Detection(Node):
    def __init__(self):
        super().__init__("detection")
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.scan_callback,
            10
        )
        self.alert_publisher = self.create_publisher(String, "obstacle_alert", 10)
        self.threshold_distance = 0.5  # アラートの閾値 (単位: メートル)

    def scan_callback(self, msg):
        # スキャンデータ内の最小距離を取得
        min_distance = min(msg.ranges)

        # 障害物が閾値以内にある場合アラートを送信
        if min_distance < self.threshold_distance:
            alert_msg = String()
            alert_msg.data = f"Obstacle detected at {min_distance:.2f} meters!"
            self.alert_publisher.publish(alert_msg)
            self.get_logger().warn(alert_msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = Detection()
    rclpy.spin(node)
    
