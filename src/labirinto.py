#! /usr/bin/env python
# -*- coding:utf-8 -*-


import time
from robot_control_class import RobotControl #importa classe

class Robo(RobotControl, object):
	def __init__(self):
		# pega os atributos da classe RobotControl
		super(Robo,self).__init__()

		print("inicializando...")
		self.robotmove_speed = 0.22
		self.robotmove_time = 1
		self.robotturn_clockwise = "clockwise"
		self.robotturn_speed = 2.84
		self.robotturn_time = 3
		self.laser1 = []
	

	def robotinicio(self):
		robo.stop_robot()
		print("...")
		print("estou pronto! ")

	def robotmove(self):
		robo.move_straight()
		while robo.get_front_laser() > 1:
			robo.move_straight()
			#print("distancia: ", robotcontrol.get_front_laser())

		robo.stop_robot()
		#print("estou perto demais da parede... ")

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
	robo.robotinicio() #inicializa o robo
	try:
		while not robo.ctrl_c:
			robo.robotmove()
			robo.robotturn()

	except rospy.ROSInterruptException:
		pass
	




