#Made by Jackson Lohman and TJ Reynolds 2018
#runs on the ground
import arrow
import socket
import time
import serial

#----- GLOBAL VARS -----#
function = int(input('Which would you like to communicate with: \n 0: Phobos and Deimos \n 1: LoRa \n '))
gps_input = ''
f = open("", "a") #add filepath to whatever the .txt is
NetworkPort = 59281
command = 1
#-----------------------#

def selection():
	if function == 0:
		rpi.run_socket()
	elif function == 1:
		lora.run_format()
	else:
		print('Invalid Input, Try Again')
		selection()

class lora(): #NEED to still to make it so that it brings in new gps data
	def format_data(input):
		date = arrow.now().format('MM/DD/YYYY')
		time = arrow.now().format('HH:mm:ss')
		final_time = 'Time: ' + time + " " + date + ' MST'
		print('\n'+str(final_time))
		f.write('\n\n'+str(final_time))

		lat = input[18:29] 
		deg_lat = lat[:2]
		sec_lat = lat[2:9]
		dir_lat = lat[10:]
		final_lat = 'Latitude: '+deg_lat+'° '+sec_lat+"' " +dir_lat
		print(str(final_lat))
		f.write('\n'+str(final_lat))

		long = input[30:42] 
		deg_long = long[:3]
		sec_long = long[3:10]
		dir_long = long[11:]
		final_long = 'Longitude: '+deg_long+'° '+sec_long+"' " +dir_long
		print(str(final_long))
		f.write('\n'+str(final_long))

		alt = input[52:59] 
		length = alt[0:5]
		final_alt = 'Altitude: '+length+' meters'
		print(str(final_alt))
		f.write('\n'+str(final_alt))

		hdop = input[47:51]
		final_hdop = 'Postition accuracy: '+hdop+' meters'
		print(str(final_hdop))
		f.write('\n'+str(final_hdop))

	def getdata():
		ser = serial.Serial('/dev/ttyACM0', 9600) #change ACM0 to what ever it shows up as when feather is conected to linux laptop
		ser.baudrate = 9600
		readser = ser.readline().decode()
		data = str(readser)
		start = data[:6]
		if start == '$GPGGA':
			print(data)
			lora.format_data(data)
		else:
			print('Incomplete Data... Trying Again')
			lora.getdata()
		return data

	def run_format():
		while True:
			lora.getdata()
			
class rpi(): #turns on and off camera
	def socketSend():
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind(('', NetworkPort))#accept any ip address
		sock.listen(1)
		print('Listening for Connection...')
		conn, addr = sock.accept()
		print('connected to' + str(addr))
		
		conn.sendall(str(command).encode())
		print('command sent')
		sock.close()

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind(('', NetworkPort))#accept any ip address
		sock.listen(1)
		print('Listening for Connection...')
		conn, addr = sock.accept()
		print('connected to' + str(addr))
		
		conn.sendall(str(command).encode())
		print('command sent')
		sock.close()

	def run_socket():
		rpi.socketSend()

selection()
