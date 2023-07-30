int tempo = 60;
int distanceCm = 15;
int mode = 1;

int i = 0;
int dummy = 100;


void setup() {
  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {

  // sensor geting data...
  delayMicroseconds(2);
  delayMicroseconds(10);

  // software delay
  i += 1;
  if (i == dummy) {
    i = 0;
    distanceCm += 10;
    if (distanceCm >= 80) distanceCm = 15;
  }


  // Send {delay, distance} to the Serial Monitor
  Serial.print(tempo);
  Serial.print("bpm, ");
  Serial.print(distanceCm);
  Serial.print("cm, mode=");
  Serial.println(mode);

  delay(10);
}