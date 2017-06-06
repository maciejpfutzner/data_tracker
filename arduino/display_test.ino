#include "SevSeg.h"

int number;
int i, buzzCount;
int dp;
int frequency;
int redLED;
int greenLED;
int alarmON;
int alarmCount;
int redON;
int greenON;
int buttonPin;
int buttonState;
int lastButtonState;

SevSeg sevseg; //Initiate a seven segment controller object

void setup()
{

  // Setup display

  byte numDigits = 4;

  number = 0;
  i = 1000;
  dp = 0;
  buzzCount = 0;
  redLED = A1;   //Set this
  greenLED = A2; //Set this
  alarmON = 0;
  alarmCount = 10000;
  redON = 0;
  greenON = 0;
  buttonPin = -1; //Set this
  buttonState = 0;
  lastButtonState = 0;

  byte digitPins[] = {2, A5, 4, 5};

  byte segmentPins[] = {6, 7, 8, 9, 10, 11, 12, 13};

  sevseg.begin(COMMON_CATHODE, numDigits, digitPins, segmentPins);

  sevseg.setBrightness(90);

  // Setup python interface

  Serial.begin(9600);      // set the baud rate
  Serial.println("Ready"); // print "Ready" once

  // Setup red and green LEDs

  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void decode(char inByte)
{
  switch (inByte)
  {
    case 'n':
      i = 1000;
      number = 0;
      break;
    case 'b':
      buzzCount = 1000;
      break;
    case 'r':
      digitalWrite(redLED, HIGH);
      redON = 1;
      break;
    case 'g':
      digitalWrite(greenLED, HIGH);
      greenON = 1;
      break;
    case 'c':
      alarmON = 0;
      break;
    case 'a':
      alarmON = 1;
      break;
    case 'o':
      digitalWrite(redLED, LOW);
      digitalWrite(greenLED, LOW);
      redON = 0;
      greenON = 0;
      break;
    default:
      if (i == 3) {
        dp = inByte - 48;
      } else {
        int digit = inByte - 48;
        number = number + (digit * i);
        if (i == 1)
        {
          i = 30;
        }
        i = i / 10;
      }
  }
}

void loop()
{

  /**char c;
    c = Serial.read();
    int number = 0;
    if (c == 'A') number = 5555;
    //sevseg.setChars(c);**/
  //digitalWrite(A0, HIGH);
  char inByte = ' ';
  if (Serial.available())
  {                         // only send data back if data has been sent
    inByte = Serial.read(); // read the incoming data
    decode(inByte);
    //Serial.println(inByte); // send the data back in a new line so that it is not all one long line
    //Serial.println(number);
  }

  /**while (Serial.available()) {
    number = ( Serial.read() - 245 ) * 1000 ;
    Serial.println(number);
    number = number + ( Serial.read() - 245 ) * 100 ;
    Serial.println(number);
    }**/

  sevseg.setNumber(number, dp);
  //sevseg.setChars(c);
  sevseg.refreshDisplay(); // Must run repeatedly

  if (buzzCount > 0)
  {
    tone(3, 10000);
    buzzCount--;
  }
  else
  {
    noTone(3);
  }
  //frequency = analogRead(A0) * 5 + 1000;

  buttonState = digitalRead(buttonPin);
  // compare the buttonState to its previous state
  if (buttonState != lastButtonState)
  {
    alarmON = 0;
    // Delay a bit to avoid bouncing
    delay(50);
  }
  // save the current state as the last state,
  //for next time through the loop
  lastButtonState = buttonState;

  // Alarm code
  if (alarmON)
  {
    if (alarmCount < 3000)
    {
      noTone(3);
      if (redON)
      {
        digitalWrite(redLED, LOW);
      }
      if (greenON)
      {
        digitalWrite(greenLED, LOW);
      }
    }
    else
    {
      tone(3, 3000);
      if (redON)
      {
        digitalWrite(redLED, HIGH);
      }
      if (greenON)
      {
        digitalWrite(greenLED, HIGH);
      }
    }
    --alarmCount;
    if (alarmCount == 0)
    {
      alarmCount = 6000;
    }
  }
}
