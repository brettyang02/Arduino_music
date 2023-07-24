// Constants for ultrasonic sensor pins
const int trigPin = 9;   // Trig pin connected to digital pin 9
const int echoPin = 10;  // Echo pin connected to digital pin 10

void setup() {
  Serial.begin(9600);    // Initialize serial communication at 9600 baud rate
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  long duration, distance;  // Variables to store the duration and calculated distance

  // Clear the trigPin state to trigger the ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Set the trigPin high for 10 microseconds to send the ultrasonic pulse
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure the time it takes for the pulse to return (echo)
  duration = pulseIn(echoPin, HIGH);

  // Calculate the distance based on the speed of sound (343 meters per second) and time of flight
  distance = (duration / 2) * 0.0343;

  // Print the distance to the object in centimeters on the serial monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Add a delay before the next measurement
  delay(10);  // You can adjust this delay to control the update rate of distance readings
}