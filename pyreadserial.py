import serial

ser = serial.Serial('/dev/ttyACMO', 9600)
ser.baudrate = 9600

while True:
  read_ser = ser.readline()
  print(read_ser) #need to get rid of b' and '\r\n on each output line
