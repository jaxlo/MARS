// Made by Jackson Lohman and TJ Reynolds 2019
// Part of this code is borrowed from adafruit.com and https://github.com/robertsmarty/adafruit3078gps/blob/master/Adafruit%20Feather%2032u4%20LoRa/GPS_TX.ino#L80

#include <SPI.h>
#include <RH_RF95.h>
 
#define RFM95_CS 8
#define RFM95_RST 4
#define RFM95_INT 3


// TX must match RX's freq!
#define RF95_FREQ 915.0
 
// Singleton instance of the radio driver
RH_RF95 rf95(RFM95_CS, RFM95_INT);
 
// Blinky on receipt
#define LED 13
 
void setup() 
{
// Configure onboard LED
  pinMode(LED, OUTPUT); 

// Configure reset pin for output
  pinMode(RFM95_RST, OUTPUT);


// Configure GPS serial port
  Serial1.begin(9600);

// Configure serial port for debugging
  Serial.begin(9600);
  delay(100);
 
// Reset the radio
  digitalWrite(RFM95_RST, LOW);
  delay(10);
  digitalWrite(RFM95_RST, HIGH);
  delay(10);

// Initialize radio 
  rf95.init();

// Set frequency, power and slow-long range
  rf95.setFrequency(RF95_FREQ);
  rf95.setTxPower(23, false);
}
 
void loop()
{
  char radiodata[1000],c=0;
  String gpsdata,year;

// Read data from GPS module until end of line  
  c=0;
  while(c !=10) {
    if(Serial1.available()) {
      c=Serial1.read();
      gpsdata+=c;
      //Serial.print(c);
    }
  }
  Serial.print(gpsdata);
  gpsdata.toCharArray(radiodata, gpsdata.length()+1);
  rf95.send((uint8_t *)radiodata, gpsdata.length()+1);
  rf95.waitPacketSent();

}
