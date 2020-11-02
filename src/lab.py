#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
import time
from geometry_msgs.msg import Twist


def main():
	cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=3)
	rospy.init_node("anda_e_para")
	para = Twist()
	anda = Twist()
	anda.linear.x = 0.2

	anda_frente = False

	tempo_andando = rospy.Time.now()
	rate = rospy.Rate(1)
	rospy.loginfo("carregado")


	while not rospy.is_shutdown():
		rospy.loginfo("cmd_vel publicado - anda: "+str(anda_frente))
		if anda_frente:
			cmd_vel_pub.publish(anda)			
		else:
			cmd_vel_pub.publish(para)

		if  rospy.Time.now() > tempo_andando:
			anda_frente = not anda_frente
			tempo_andando = rospy.Time.now() + rospy.Duration(5)
		rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass