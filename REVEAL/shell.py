import serial
import re
import time
import subprocess

ser = serial.Serial('COM3', 9600)

delay = 0; distance = 0; mode = 0
tempo = 0
note = 0
time_old = 0
current = None


while True:
    # read datq from serial port
    # if run=0, will just wait until data is available
    data = ser.readline().decode().strip()

    # find the three integers in the string
    pattern = r'\d+'
    numbers = re.findall(pattern, data)
    [delay, distance, mode] = [int(num) for num in numbers]

    if (delay >= 2000):
        tempo = 30
    elif (1500 <= delay < 2000):
        tempo = 40
    elif (1000 <= delay < 1500):
        tempo = 60
    else:
        tempo = 120

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
        current = subprocess.Popen(["python", "REVEAL/play.py", str(note), str(mode), str(tempo), str(distance)])
        time_old = time_new