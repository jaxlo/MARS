// Made by Jackson Lohman and TJ Reynolds 2018
// Part of this code is borrowed from adafruit.com

#include <SPI.h>
#include <RH_RF95.h>

//for feather m0  
#define RFM95_CS 8
#define RFM95_RST 4
#define RFM95_INT 3


// Change to 434.0 or other frequency, must match RX's freq!
#define RF95_FREQ 434.0

// Singleton instance of the radio driver
RH_RF95 rf95(RFM95_CS, RFM95_INT);

#define GPSSerial Serial1

void setup() 
{

  GPSSerial.begin(9600);
  
  pinMode(RFM95_RST, OUTPUT);
  digitalWrite(RFM95_RST, HIGH);

  Serial.begin(115200);
 
 

  // manual reset
  digitalWrite(RFM95_RST, LOW);
  delay(10);
  digitalWrite(RFM95_RST, HIGH);
  delay(10);

  while (!rf95.init()) {
    Serial.println("LoRa radio init failed");
    while (1);
  }
  Serial.println("LoRa radio init OK!");

  // Defaults after init are 434.0MHz, modulation GFSK_Rb250Fd250, +13dbM
  if (!rf95.setFrequency(RF95_FREQ)) {
    Serial.println("setFrequency failed");
    while (1);
  }
  Serial.print("Set Freq to: "); Serial.println(RF95_FREQ);
  
  // Defaults after init are 434.0MHz, 13dBm, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on

  // The default transmitter power is 13dBm, using PA_BOOST.
  // If you are using RFM95/96/97/98 modules which uses the PA_BOOST transmitter pin, then 
  // you can set transmitter powers from 5 to 23 dBm:
  rf95.setTxPower(23, false);
}

int16_t packetnum = 0;  // packet counter, we increment per xmission

void loop()
{
  String line;
  char c = GPSSerial.read();
  Serial.write(c); // remove write line (or comment out) so that it doesnt try to write to serial before sending over lora
  //delay(250); // Wait 1 second between transmits, could also 'sleep' here!
  //Serial.println("\nTransmitting..."); // Send a message to rf95_server
  
  //char radiopacket[20] = "Hello World #      ";
  //itoa(packetnum++, radiopacket+13, 10);
  //Serial.print("\nSending "); Serial.println(c);
  //radiopacket[19] = 0;
  
  //Serial.println("Sending...");
  //delay(10);
  rf95.send((uint8_t *)c, 1000);

  //Serial.println("\nWaiting for packet to complete..."); 
  rf95.waitPacketSent();
  
  
  

}
