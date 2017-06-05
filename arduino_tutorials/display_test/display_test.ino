#include "SevSeg.h"

SevSeg sevseg; //Initiate a seven segment controller object

void setup() {

  // Setup display

  byte numDigits = 4;

  byte digitPins[] = {2, 3, 4, 5};

  byte segmentPins[] = {6, 7, 8, 9, 10, 11, 12, 13};

  sevseg.begin(COMMON_CATHODE, numDigits, digitPins, segmentPins);

  sevseg.setBrightness(90);

  // Setup python interface

  Serial.begin(9600); // set the baud rate
  Serial.println("Ready"); // print "Ready" once


}

void loop() {

  /**char c;
    c = Serial.read();
    int number = 0;
    if (c == 'A') number = 5555;

    //sevseg.setChars(c);**/  
  int i = 3;
  int number = 0;
  char inByte = ' ';
  while (Serial.available()) { // only send data back if data has been sent
    int inByte = Serial.read(); // read the incoming data
    if ( i == 0 ) {
      number = number + 9;
    }
    else {
      number = number + (9 * pow(10,i));
    }
    Serial.println(inByte); // send the data back in a new line so that it is not all one long line
    Serial.println(number);
    --i;
  }

  /**while (Serial.available()) {
    number = ( Serial.read() - 245 ) * 1000 ;
    Serial.println(number);
    number = number + ( Serial.read() - 245 ) * 100 ;
    Serial.println(number);
    }

    sevseg.setNumber(number, 3);
    //sevseg.setChars(c);
    sevseg.refreshDisplay(); // Must run repeatedly**/
}

