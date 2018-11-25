#Made by Jackson Lohman and TJ Reynolds in 2018
#camera program for the raspberry pi 
import time
from picamera import picamera
import socket

comp = int(input('which computer: \n 0: Deimos \n 1: Phobos \n'))

start_time = time.time()
time_save = 1200 #20min

filename = ''
start = 0 #set to 1 to meet conditions below
stop = 0 #set to 1 to meet conditions below

NetworkHost = '192.168.1.135' #add ip of laptop
NetworkPort = 59281

try:
	picam = PiCamera()
	if comp == 0:
		picam.resolution = (1920,1080)
		picam.framerate = 30
		filename = 'deimos'
	elif comp == 1:
		picam.resolution = (1280,720)
		picam.framerate = 60
		filename = 'phobos'		
	else:
		pass
	picam.start_preview()#comment out if not connected to an external monitor
	camSupport = True
	print('picam enabled')
	time.sleep(5)
except ImportError:
	camSupport = False
	print('picam disabled')

class record():
	def start():
		start = socketListen()
		if start == 1:
			picam.start_recording('/home/MARS/'+filename+'cam.h264')
		else:
			print('Invalid, please try again')
			record.start()
	
	def stop():#will need to do threading for the stop portion
		condition = True
		while condition == True:
			connection = checkConnection()
			if connection == True:
				stop = socketListen()
				if stop == 1:
					picam.stop_recording()
					picam.stop_preview()#comment out if not connected to an external monitor
					condition = False
				else:
					print('Invalid, please try again')
					record.stop()
			elif connection == False:
				if time.time() > start_time + time_save:
					picam.stop_recording()
					picam.stop_preview()#comment out if not connected to an external monitor
					condition = False
				else:
					pass
			else:
				pass

def checkConnection(host = '192.168.1.135', port = 59281, timeout = 3): #change to ip address of laptop
	try:
		socket.setdefaulttimeout(timeout)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		print('Connected to internet')
		return True
	except:
		print('Not connected to internet')
		return False

def socketListen():

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
		sock.connect((NetworkHost, NetworkPort))
		data = sock.recv(1024)
	print('Received: ', str(data.decode()))
	sock.close()
	precommand = str(data.decode())
	command = int(precommand)
	return command

record.start()
print('Disconnect the Raspberry Pi from the internet')
time.sleep(60) #Makes sure that the rpi can be disconnected from wifi before it checks the internet connecton to stop recording
record.stop()
