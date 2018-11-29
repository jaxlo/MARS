#Made by Jackson Lohman and TJ Reynolds 2018
#runs on the ground
import arrow
import socket
import time

#----- GLOBAL VARS -----#
function = int(input('Which would you like to communicate with: \n 0: Phobos and Deimos \n 1:LoRa'))
gps_input = ''
f = open("C:\\Users\\reyno\\Documents\\marsgps.txt", "a") #change to whatever the .txt is
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
	def format_data():
		date = arrow.now().format('MM/DD/YYYY')
		time = gps_input[7:13]
		hour = time[:2]
		az_hour = str(int(hour) - 7)
		minute = time[2:4]
		second = time[4:]
		final_time = 'Time: '+ az_hour+':'+minute+':'+second+' '+date +' MST'
		print('\n'+str(final_time))
		f.write('\n\n'+str(final_time))
		f.close()

		lat = gps_input[14:24]
		deg_lat = lat[:2]
		sec_lat = lat[2:8]
		dir_lat = lat[9:]
		final_lat = 'Latitude: '+deg_lat+'° '+sec_lat+"' " +dir_lat
		print(str(final_lat))
		f.write('\n'+str(final_lat))
		f.close()

		long = gps_input[25:36]
		deg_long = long[:3]
		sec_long = long[3:9]
		dir_long = long[10:]
		final_long = 'Longitude: '+deg_long+'° '+sec_long+"' " +dir_long
		print(str(final_long))
		f.write('\n'+str(final_long))
		f.close()

		alt = gps_input[46:53]
		length = alt[0:5]
		final_alt = 'Altitude: '+length+' meters'
		print(str(final_alt))
		f.write('\n'+str(final_alt))
		f.close()

	def run_format():
		while True:
			gps_input = "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"  #need to change to get a new reading (probably function call)
			lora.format_data()
			
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
