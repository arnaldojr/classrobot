#!/usr/bin/env python
# -*- coding:utf-8 -*-


#   exemplo adaptado do livro:
#   
#  Programming Robots with ROS.
#  A Practical Introduction to the Robot Operating System
#  Example 12-5. follower_p.py pag265

import rospy
import numpy as np
import math
import cv2
import time
from sensor_msgs.msg import Image, CompressedImage, LaserScan
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge, CvBridgeError

class Follower:

    def __init__(self):
        
        self.bridge = CvBridge()
        self.cv_image = None
        self.image_sub = rospy.Subscriber('/camera/image/compressed',
                                            CompressedImage, 
                                            self.image_callback, 
                                            queue_size=4, 
                                            buff_size = 2**24)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel',
                                            Twist, 
                                            queue_size=1)
        
        self.laser_subscriber = rospy.Subscriber('/scan',
                                                 LaserScan, 
			                                    self.laser_callback)
        
        self.twist = Twist()
        self.laser_msg = LaserScan()

    def laser_callback(self, msg):
        self.laser_msg = msg

    def get_laser(self, pos):
        return self.laser_msg.ranges[pos]
    
    def process_image(self, image):
        self.filter_image(imgage)

    def filter_image(self, image):
        
        self.hsv = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2HSV)
        self.lower_yellow = np.array([22, 50, 50],dtype=np.uint8)
        self.upper_yellow = np.array([36, 255, 255],dtype=np.uint8)
        self.mask = cv2.inRange(hsv, lower_yellow, upper_yellow)


    def image_callback(self, msg):
        
        try:
            self.cv_image = self.bridge.compressed_imgmsg_to_cv2(msg,desired_encoding='bgr8')



            h, w, d = cv_image.shape
            search_top = 3*h/4
            search_bot = 3*h/4 + 20
            mask[0:search_top, 0:w] = 0
            mask[search_bot:h, 0:w] = 0
            M = cv2.moments(mask)
            if M['m00'] > 0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.circle(cv_image, (cx, cy), 20, (0,0,255), -1)
                # BEGIN CONTROL P Gain
                err = cx - w/2
                self.distancia_frente = self.get_laser(0)
                if self.distancia_frente > 1:
                    self.twist.linear.x = 0.2*self.distancia_frente*
                elif 0.2 < self.distancia_frente < 1:
                    self.twist.linear.x = 0.2*self.distancia_frente
                else:
                    self.twist.linear.x = 0.0

#                self.twist.linear.x = 0.2
                self.twist.angular.z = -float(err) / 100
                self.cmd_vel_pub.publish(self.twist)
                # END CONTROL
            cv2.imshow("window", cv_image)
            cv2.waitKey(1)
        except CvBridgeError as e:
            print('ex', e)

rospy.init_node('follower')
follower = Follower()
rospy.spin()
# END ALL