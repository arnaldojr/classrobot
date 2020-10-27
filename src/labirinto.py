#! /usr/bin/env python
# -*- coding:utf-8 -*-

import robot_control_class
#import time
from robot_control_class import RobotControl #importa uma classe

robotcontrol = RobotControl()

#criando um objeto

class Robo:

	def __init__(self):
		print("inicializando...")
		
		self.robotmove_speed = 0.2
		self.robotmove_time = 1
		self.robotturn_clockwise = "clockwise"
		self.robotturn_speed = 0.2
		self.robotturn_time = 3
		self.laser1 = []

	def robotinicio(self):
		print("configurando... ")
		robotcontrol.stop_robot()
		robotcontrol.move_straight()
		robotcontrol.turn("aclockwise", self.robotturn_speed, self.robotturn_time)
		robotcontrol.stop_robot()
		print("estou pronto! ")

	def robotmove(self):
		robotcontrol.move_straight()
		while robotcontrol.get_front_laser() > 1:
			robotcontrol.move_straight()
			print("distancia: ", robotcontrol.get_front_laser())

		robotcontrol.stop_robot()
		print("estou perto demais da parede... ")

	def robotturn(self):
		distancia_direita = robotcontrol.get_laser(45)
		distancia_esquerda = robotcontrol.get_laser(360-45)
		print("direita",distancia_direita, "esquerda", distancia_esquerda)
		if distancia_direita > distancia_esquerda:
			while self.laser1 < 1:
				robotcontrol.turn(self.robotturn_clockwise, self.robotturn_speed, self.robotturn_time)
				self.laser1 = robotcontrol.get_laser(360)
				print("direita: distancia: ", self.laser1)
		else:
			while self.laser1 < 1:
				robotcontrol.turn("aclockwise", self.robotturn_speed, self.robotturn_time)
				self.laser1 = robotcontrol.get_laser(360)
				print("esquerda: distancia: ", self.laser1)

		robotcontrol.stop_robot()
		print("ja virei, bora... ")

if __name__ == '__main__':

	robo = Robo()
	robo.robotinicio()
	while not robotcontrol.ctrl_c:
		robo.robotmove()
		robo.robotturn()
