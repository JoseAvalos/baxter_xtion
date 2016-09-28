#!/usr/bin/env	python
import	rospy
from	sensor_msgs.msg	import	Image
import 	cv2, cv_bridge
import 	numpy as np
import 	argparse

class	Follower:
		def	__init__(self):
				self.bridge	=	cv_bridge.CvBridge()
				#cv2.namedWindow("window",	1)
				self.image_sub	=	rospy.Subscriber('camera/rgb/image_raw',
																																						Image,	self.image_callback)
		def	image_callback(self,	msg):
				boundaries = [
					([17, 15, 120], [50, 56, 250]),
					([86, 31, 4], [200, 88, 70]),
					#([25, 146, 190], [62, 174, 250]),
					#([103, 86, 65], [145, 133, 128])
				]

				image	=	self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
				for (lower, upper) in boundaries:
					# create NumPy arrays from the boundaries
					lower = np.array(lower, dtype = "uint8")
					upper = np.array(upper, dtype = "uint8")
				 
					# find the colors within the specified boundaries and apply
					# the mask
					mask = cv2.inRange(image, lower, upper)
					output = cv2.bitwise_and(image, image, mask = mask)
					moments = cv2.moments(mask)
    				area = moments['m00']
				print "moment= ", area
				if(area > 300000):
					x = int(moments['m10']/moments['m00'])
					y = int(moments['m01']/moments['m00'])
				         
				        #Mostramos sus coordenadas por pantalla
				print "x = ", x
				print "y = ", y
				 
				        #Dibujamos una marca en el centro del objeto
				cv2.circle(image, (x, y), 10,(255,0,0), 2)
				#cv2.imshow("window",	image)
				cv2.imshow("images", np.hstack([image, output]))
				#(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
				#c = max(cnts, key = cv2.contourArea)
				#return cv2.minAreaRect(c)
				cv2.waitKey(5)
		#def find_marker(image):
				# convert the image to grayscale, blur it, and detect edges
				 
				# find the contours in the edged image and keep the largest one;
				# we'll assume that this is our piece of paper in the image
				
			 
				# compute the bounding box of the of the paper region and return it
				

rospy.init_node('follower')
follower	=	Follower()
rospy.spin()





