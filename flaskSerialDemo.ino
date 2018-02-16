#include "Wire.h"
#include "Adafruit_LiquidCrystal.h"

Adafruit_LiquidCrystal lcd(0);

String inString = "";
long timeThis, timeLast;

void setup() {
	Serial.begin(115200);
	lcd.begin(16, 2);
}

void loop() {
	timeThis = millis();
	if (timeThis - timeLast >= 1000) {
		Serial.print("345,222,321,443,T");
		timeLast = timeThis;
	}

	if (Serial.available()) {
		char inChar = Serial.read();	
		if (isDigit(inChar)) {
			inString += inChar;
		}
		else if (inChar == ',') {
			lcd.print(inString);
			lcd.print(':');
			inString = "";
		}
		else if (inChar == 'T') {
			lcd.print("            ");
			lcd.setCursor(0,0);
		}
	}
}	
