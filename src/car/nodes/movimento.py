#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PointStamped
from nav_msgs.msg import Odometry

class Movimento:
    def __init__(self):
        rospy.init_node('movimento_carro', anonymous=True)
        rospy.Subscriber('odom_nemo', Odometry, self.posicaoCarroVerde)
        rospy.Subscriber('sonar_data', PointStamped, self.posicaoRelativaEntreCarros)
        rospy.Subscriber('odom', Odometry, self.posicaoAtual)
        self.pubMovimentacao = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.odomNemo = Odometry()
        self.posicaoRelativaCarros = PointStamped()
        self.odomCarro = Odometry()

    def posicaoCarroVerde(self,odom):

        rate = rospy.Rate(20)
        self.odomNemo = odom

        v = Twist()
        v.linear.x = odom.twist.twist.linear.x
        v.linear.y = odom.twist.twist.linear.y
        v.linear.z = odom.twist.twist.linear.z

        v.angular.x = odom.twist.twist.angular.x
        v.angular.y = odom.twist.twist.angular.y
        v.angular.z = odom.twist.twist.angular.z

        self.pubMovimentacao.publish(v)
        
        rate.sleep()

    def posicaoAtual(self,odomCarro):

        rate = rospy.Rate(10)
        self.odomCarro = odomCarro

        rate.sleep()

    #Distância que o carro tem que percorrer
    def posicaoRelativaEntreCarros(self,posicaoRelativa):
        rate = rospy.Rate(5)
        self.posicaoRelativaCarros = posicaoRelativa

        rate.sleep()



if __name__ == '__main__':
    try:
        t = Movimento()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass    