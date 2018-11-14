#By Jackson Lohman and TJ Reynolds in 2018

try:
	from picamera import PiCamera
	picam = PiCamera()
	picam.resolution = (320,320)#run now to give it time to load, change reslution
	camSupport = True
	print('Pi Camera Enabled')
except ImportError:
	camSupport = False
	print('Pi Camera Disabled')
  
def socketListen():
  pass
def socketSend():
 pass
def Record():
  pass
