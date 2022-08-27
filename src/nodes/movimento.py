#!/usr/bin/env python3

import rospy
from geometry_msgs import Twist
import random

class Movimento:
    def __init__(self):
        rospy.init_node('movimento_carro', anonymous=True)
        rospy.Subscriber('odom_nemo', Twist, self.movimentarCarro)
        self.pubMovimentacao = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    def movimentarCarro(self,msg):
        rate = rospy.Rate(5)
        v = Twist()
        v.linear.x = msg.twist.twist.linear.x
        v.linear.y = msg.twist.twist.linear.y
        v.linear.z = msg.twist.twist.linear.z

        v.angular.x = msg.twist.twist.angular.x
        v.angular.y = msg.twist.twist.angular.y
        v.angular.z = msg.twist.twist.angular.z


        self.pubMovimentacao.publish(v)
        rate.sleep()


if __name__ == '__main__':
    try:
        t = Movimento()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass    