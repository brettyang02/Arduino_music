#include <Keypad.h>

// Constants for HC-SR04 pins
const int trigPin = 2;
const int echoPin = 3;

// Define the keypad layout
const byte ROWS = 4; //four rows
const byte COLS = 4; //four columns
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte rowPins[ROWS] = {4, 5, 6, 7}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {8, 9, 10, 11}; //connect to the column pinouts of the keypad
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

// Variables
long duration;
int distanceCm;
unsigned long delayBuffer = 0;
unsigned long delayTime = 1000; // Default delay of 1000ms (1 second)
unsigned long previousMillis = 0;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Set trigPin as OUTPUT and echoPin as INPUT
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {

  // Convert keypad input (ends with '#') t0 number
  char key = keypad.getKey();
  if (key >= '0' && key <= '9') {
    delayBuffer = delayBuffer * 10 + (key - '0');
  }
  else if (key == '#'){
    delayTime = delayBuffer;
    delayBuffer = 0;
  }

  // Perform distance measurement when the required delay has passed
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= delayTime) {
    // Clear the trigPin to ensure a clean pulse
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    // Trigger the sensor by sending a 10us pulse on trigPin
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    // Measure the duration of the pulse received on echoPin
    duration = pulseIn(echoPin, HIGH);

    // Calculate the distance in centimeters
    // Sound travels at 343 meters per second in air (at 20 degrees Celsius).
    // Divide by 2 to account for the time taken to reach the object and return to the sensor.
    distanceCm = duration * 0.0343 / 2;

    // Send {delay, distance} to the Serial Monitor
    Serial.print(delayTime);
    Serial.print("ms, ");
    Serial.print(distanceCm);
    Serial.print("cm \n");
    // Reset the timer for the next measurement
    previousMillis = currentMillis;
  }
}

