#! /usr/bin/env python
# -*- coding:utf-8 -*-

#https://raw.githubusercontent.com/StevenShiChina/books/master/ros%20by%20example%20vol%201%20indigo.pdf
#https://raw.githubusercontent.com/StevenShiChina/books/master/ros%20by%20example%20vol%202%20indigo.pdf
#file:///home/borg/Downloads/Programming.Robots.with.ROS.A.Practical.Introduction.to.the.Robot.Operating.System.pdf
#https://github.com/Art-robot0/omniWheelCareRobot-usual/blob/ca175a0e91bf971a1e8a449c34ef75536bb60844/rosCode/src/carebot_tasks/nodes/patrol_script.py
#https://github.com/longbowliu/robotStudy/blob/8fe7eb2f04cf16d497278caf1193a8041c6fb4e7/rbx2-indigo-devel/rbx2_tasks/nodes/patrol_script.py


import time
from robot_control_class import RobotControl #importa classe

class Robo(RobotControl, object):
	def __init__(self):
		# pega os atributos da classe RobotControl
		super(Robo,self).__init__()

		print("inicializando...")
		self.pos_braco = 0
		self.pos_garra = -1
		self.robotturn_clockwise = "clockwise"
		self.robotturn_speed = 2.84
		self.robotturn_time = 3
		self.laser1 = []
	

	def robotinicio(self):
		robo.stop_robot()
		print("...")
		print("estou pronto! ")

	def robotmove(self):
		while robo.get_front_laser() > 1:
			robo.move_straight()
			#print("distancia: ", robotcontrol.get_front_laser())

		robo.stop_robot()
		#print("estou perto demais da parede... ")

	def robotgarra(self):
		print("Exemplo move garra ")
		print("inicio")
		robo.move_joints_init()
		print("posição")
		robo.move_joints(self.pos_braco,self.pos_garra)
		print("sobe")
		robo.move_joints_sobe()
	

	def media_scan(self):

		media = robo.get_laser_average(0,1)
		print("media: ",media )

		robo.stop_robot()


	def robotturn(self):
		distancia_direita = robo.get_laser(45)
		distancia_esquerda = robo.get_laser(360-45)
		#print("direita",distancia_direita, "esquerda", distancia_esquerda)
		if distancia_direita > distancia_esquerda:
			while self.laser1 < 1:
				robo.turn(self.robotturn_clockwise, self.robotturn_speed, self.robotturn_time)
				self.laser1 = robo.get_laser(360)
				#print("direita: distancia: ", self.laser1)
		else:
			while self.laser1 < 1:
				robo.turn("aclockwise", self.robotturn_speed, self.robotturn_time)
				self.laser1 = robo.get_laser(360)
				#print("esquerda: distancia: ", self.laser1)

		robo.stop_robot()
		



if __name__ == '__main__':
	robo = Robo() # cria o objeto
	robo.stop_robot()
	robo.robotinicio() #inicializa o robo
	try:		
		while not robo.ctrl_c:

			robo.media_scan()
			#robo.robotgarra()
			#robo.robotturn()
			robo.rate.sleep()
	
	except rospy.ROSInterruptException:
		pass
	




