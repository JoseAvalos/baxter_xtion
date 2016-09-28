# Baxter_xtion
This project try to make computer science with the baxter ans the sensor ASUS xtion. This project use Ros-Indigo. 
All instruccion will operate in terminal. 

## [Xtion sensor] Basic Driver 
This driver just will work ok with usb 2.0
### Dependence
```
sudo apt-get install -y g++ git python libusb-1.0-0-dev libudev-dev freeglut3-dev doxygen graphviz openjdk-6-jdk
```
### Install OPENNI2 for ROS

```
sudo apt-get install ros-indigo-rgbd-launch ros-indigo-openni2-camera ros-indigo-openni2-launch
```
### Install RQT as plugin
```
sudo apt-get install ros-indigo-rqt ros-indigo-rqt-common-plugins ros-indigo-rqt-robot-plugins
```

## Testing 
Begin ROS Envioroment
```
roscore 
```
In another terminal

```
roslaunch openni2_launch openni2.launch
```
will apper the topics

```
rostopic list 
```
To reproduce 
```
rqt
```
In the window select “Plugins”  / “Visualization” / “Image View“ and choose a topic
