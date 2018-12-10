// Made by Jackson Lohman and TJ Reynolds 2018
// Part of this code is borrowed from adafruit.com

#define GPSSerial Serial1
 
 
void setup() {
  // 9600 baud is the default rate for the GPS
  GPSSerial.begin(9600);
}
 
void loop() {  
  if (GPSSerial.available()) {
    char c = GPSSerial.read();
    Serial.write(c); // remove write line (or comment out) so that it doesnt try to write to serial before sending over lora
    }
}
