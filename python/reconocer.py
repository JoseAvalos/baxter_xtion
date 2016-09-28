#!/usr/bin/env	python
import	rospy
from	sensor_msgs.msg	import	Image
import 	cv2, cv_bridge
import 	numpy as np
import 	argparse

class	Follower:
		def	__init__(self):
				self.bridge	=	cv_bridge.CvBridge()
				cv2.namedWindow("window",	1)
				self.image_sub	=	rospy.Subscriber('camera/rgb/image_raw',
																																						Image,	self.image_callback)
		def	image_callback(self,	msg):
				image	=	self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
				gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
				gray = cv2.GaussianBlur(gray, (5, 5), 0)
				edged = cv2.Canny(gray, 35, 125)
				cv2.imshow("window",	edged)
				#(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
				#c = max(cnts, key = cv2.contourArea)
				#return cv2.minAreaRect(c)
				cv2.waitKey(3)
		#def find_marker(image):
				# convert the image to grayscale, blur it, and detect edges
				 
				# find the contours in the edged image and keep the largest one;
				# we'll assume that this is our piece of paper in the image
				
			 
				# compute the bounding box of the of the paper region and return it
				

rospy.init_node('follower')
follower	=	Follower()
rospy.spin()





