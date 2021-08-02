import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from cbm_interfaces.msg import AdcRaspi

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(AdcRaspi, 'topic', self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):
            self.get_logger().info('I heard: "%f, %f, %f, %f, %f, %f, %f, %f"' % 
            (msg.ch0, msg.ch1, msg.ch2, msg.ch3, msg.ch4, msg.ch5, msg.ch6, msg.ch7)) # CHANGE


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()