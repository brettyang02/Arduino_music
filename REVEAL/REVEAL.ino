#include <Keypad.h>

// Constants for pins
const int trigPin = 12;
const int echoPin = 13;

// Define the keypad layout
const byte ROWS = 4; //four rows
const byte COLS = 4; //four columns
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte rowPins[ROWS] = {2, 3, 4, 5}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {6, 7, 8, 9}; //connect to the column pinouts of the keypad
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

// Variables
long duration;
int tempo = 60;
int tempoInput = 0;
int distanceCm = 0;
int mode = 1; // [1, 2, 3, 4] for [4/4, 4/4, 3/4, 12/8]
bool run = false;
int pos = 0;

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
    tempoInput = tempoInput * 10 + (key - '0');
  }
  else if (key == '#'){
    tempo = tempoInput;
    tempoInput = 0;
  }
  else if (key == '*') {run = !run;}
  else if (key == 'A') {mode = 1;}
  else if (key == 'B') {mode = 2;}
  else if (key == 'C') {mode = 3;}
  else if (key == 'D') {mode = 4;}

  if (run) {
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

    // Send {tempo, distance, mode} to the Serial Monitor
    Serial.print(tempo);
    Serial.print("bpm, ");
    Serial.print(distanceCm);
    Serial.print("cm, mode=");
    Serial.println(mode);

    delay(10);
  } 
}
