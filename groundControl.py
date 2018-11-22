#Made by Jackson and TJ in 2018
#Takes GPS output and formats it into a more readable format
import arrow
gps_input = "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"
#would start blank
f = open("C:\\Users\\reyno\\Documents\\marsgps.txt", "a") #change to whatever the .txt is

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

	lat = gps_input[14:24]
	deg_lat = lat[:2]
	sec_lat = lat[2:8]
	dir_lat = lat[9:]
	final_lat = 'Latitude: '+deg_lat+'° '+sec_lat+"' " +dir_lat
	print(str(final_lat))
	f.write('\n'+str(final_lat))

	long = gps_input[25:36]
	deg_long = long[:3]
	sec_long = long[3:9]
	dir_long = long[10:]
	final_long = 'Longitude: '+deg_long+'° '+sec_long+"' " +dir_long
	print(str(final_long))
	f.write('\n'+str(final_long))

	alt = gps_input[46:53]
	length = alt[0:5]
	final_alt = 'Altitude: '+length+' meters'
	print(str(final_alt))
	f.write('\n'+str(final_alt))


while True:
	format_data()
	gps_input = "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47" 
	#would be new reading
