#!/usr/bin/env	python
import	rospy
from	sensor_msgs.msg	import	Image
import 	cv2, cv_bridge
import 	numpy as np
import 	argparse

class	Follower:
		def	__init__(self):
				self.bridge	=	cv_bridge.CvBridge()
				self.image_sub	=	rospy.Subscriber('camera/rgb/image_raw',
																																						Image,	self.image_callback)
		def	image_callback(self,	msg):
				cap	=	self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')

				cv2.namedWindow('Configuracion')
				#cv2.createTrackbar (100, 'Configuracion', 0,256,image_callback)
			   	#cv2.createTrackbar (200, 'Configuracion', 0,256,image_callback)
				boundaries = [
					([17, 15, 120], [50, 56, 250]),
					([86, 31, 4], [200, 88, 70]),
					#([25, 146, 190], [62, 174, 250]),
					#([103, 86, 65], [145, 133, 128])
				]
								
				#cv2.createTrackbar ('S min', 'Configuracion', 0,256,nothing)
				#cv2.createTrackbar ('S max', 'Configuracion', 0,256,nothing)
				#cv2.createTrackbar ('V min', 'Configuracion', 0,256,nothing)
				#cv2.createTrackbar ('V max', 'Configuracion', 0,256,nothing)

				
			    	hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV) 
			    #Convertimos imagen a HSV
			 
			    # Aqui mostramos la imagen en blanco o negro segun el rango de colores.
			 	#bn_img = cv2.inRange(hsv, np.array((Hmin,Smin,Vmin)), np.array((Hmax,Vmax,Smax)))
			    # Limpiamos la imagen de imperfecciones con los filtros erode y dilate
			  #  bn_img = cv2.erode (bn_img,cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)),iterations = 1)
			   # bn_img = cv2.dilate (bn_img,cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)),iterations = 1)
			    # Localizamos la posicion del objeto
			    #M = cv2.moments(bn_img)
			    #if M['m00']>50000:
			     #   cx = int(M['m10']/M['m00'])
			      #  cy = int(M['m01']/M['m00'])
			    # Mostramos un circulo verde en la posicion en la que se encuentra el objeto
			       # cv2.circle (frame,(cx,cy),20,(0,255,0), 2)
			 
			 
			    # Creamos las ventanas de salida y configuracion
			    #cv2.imshow('Salida', frame)
			    #cv2.imshow('inRange', bn_img)
				#image	=	self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
				#for (lower, upper) in boundaries:
					# create NumPy arrays from the boundaries
					#lower = np.array(lower, dtype = "uint8")
					#upper = np.array(upper, dtype = "uint8")
				 
					# find the colors within the specified boundaries and apply
					# the mask
					#mask = cv2.inRange(image, lower, upper)
					#output = cv2.bitwise_and(image, image, mask = mask)
				#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
				#gray = cv2.GaussianBlur(gray, (5, 5), 0)
				#edged = cv2.Canny(gray, 35, 125)
				cv2.imshow("window",	hsv)
				#cv2.imshow("images", np.hstack([image, output]))
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





