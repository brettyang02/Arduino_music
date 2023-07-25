import serial
import re
import time
import subprocess

ser = serial.Serial('COM3', 9600)

delay = 0; distance = 0; mode = 0
note = 0
time_old = 0
current = None


while True:
    data = ser.readline().decode().strip()

    # find the three integers in the string
    pattern = r'\d+'
    numbers = re.findall(pattern, data)
    [delay, distance, mode] = [int(num) for num in numbers]

    # turn distance to a note
    note = distance // 10
    if note > 7:
        note = 8

    # play the note when it's time
    # had to use multi-threading, if not will have readout problem with time.sleep()
    time_new = time.time() * 1000
    if (time_new - time_old) > delay:
        if (current):
            current.terminate()
        current = subprocess.Popen(["python", "July24_play.py", str(note), str(mode), str(distance)])
        time_old = time_new