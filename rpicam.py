#By Jackson Lohman and TJ Reynolds in 2018
#camera program for Deimos
from time import *
from picamera import picamera
start_time = time.time()
time_save = 1200 #20min

start = 0 #set to 1 to meet conditions below
stop = 0 #set to 1 to meet conditions below

try:
	picam = PiCamera()
	picam.resolution = (1920,1080)#change to (1280,720) for Phobos
	picam.framerate = 30
	picam.start_preview()#comment out if not connected to an external monitor
	camSupport = True
	print('picam enabled')
	time.sleep(5)
except ImportError:
	camSupport = False
	print('picam disabled')

def record():
	picam_start = True
	while picam_start == True:
		start = #new input from socket (1) --- probably call socketListen() here
		if start == 1:
			picam.start_recording('/home/MARS/deimoscam.h264')
			picam_start = False
		else:
			pass

	picam_stop = True
	while picam_stop == True:
		stop = #new input from socket (1) --- probably call socketListen() here
		if stop == 1 or time.time() > start_time + time_save:
			picam.stop_recording()
			picam.stop_preview()#comment out if not connected to an external monitor
			picam_stop = False
		else:
			pass

def socketListen():
	pass
