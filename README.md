# Arduino project: Jam helper
Elizabeth Tyra Sumual,
Shuntaro Wakamatsu, 
Brett(Jiaxin) Yang

University of Toronto - 2023

## Overview:
This project consists of an Arduino-based distance sensing system that interacts with a Python-based note player to create a musical experience based on the distance measured by an ultrasonic sensor. The system reads input from a keypad to set parameters like delay time and operating mode. It then sends the collected data (delay, distance, and mode) over the serial port to a Python outer shell, which further triggers the Python code responsible for playing the notes and drum sounds.

## Components Required:

1. Arduino board (e.g., Arduino Uno)
2. Keypad module (4x4)
3. Ultrasonic distance sensor (HC-SR04)
4. Servo motor
5. Python packages: serial, re, time, subprocess, os, pygame, sys

## How to use:
1. connect
2. press * to start, again for pause/start
3. change tempo by entering delay time (in ms) and press #
4. change mode (4/4, 3/4, 12/8) by pressing ABCD


## Code files: (~/REVEAL/)
### Arduino code (REVEAL.ino)
The Arduino code handles interactions with the keypad and ultrasonic sensor. It reads input from the keypad to set the delay time and operating mode. The ultrasonic sensor measures the distance to an object, and this information, along with the delay time and mode, is sent to the Python outer shell via the serial port.

### Python Outer Shell (shell.py):
The Python outer shell acts as an intermediary between the Arduino and the Python note player. It receives data (delay, distance, and mode) from the Arduino through the serial port. The outer shell then processes this data and triggers the Python note player based on the specified delay and mode. The Python outer shell uses multi-threading to handle note playing while maintaining a smooth interaction with the Arduino.

### Python Note Player (play.py):
The Python note player is responsible for creating musical notes and drum sounds based on the received data from the outer shell. It uses the Pygame library to handle sound playback. The note player interprets the note, distance, and mode values and plays corresponding notes or sounds to create a musical experience. The note player supports different modes of operation, and it allows you to control the volume of each sound independently.

## How to use (sucks):
Setup and Execution:
Connect the Arduino to the hardware components (keypad, ultrasonic sensor, and servo motor) as described in the connections section of the Arduino code.
Upload the Arduino code to the Arduino board using the Arduino IDE.
Connect the Arduino board to the computer via a USB cable.
Install the required Python libraries (serial, pygame) for the Python Outer Shell and Python Note Player using pip.
Run the Python Outer Shell (Python_Outer_Shell.py) on the computer. Ensure the correct serial port (e.g., 'COM3') is specified in the ser = serial.Serial('COM3', 9600) line.
The Arduino will start reading input from the keypad and sending data to the Python Outer Shell.
The Python Outer Shell will process the data and trigger the Python Note Player to play notes and drum sounds based on the received data.
Important Notes:

Ensure all hardware components are properly connected to the Arduino before uploading the code.
Adjust the delay values and mode settings as needed for your musical preferences.
The provided code is a basic example and may require further modifications or enhancements for specific use cases.