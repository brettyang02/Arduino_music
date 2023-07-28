import serial
import re
import time
import subprocess

ser = serial.Serial('COM4', 9600)

delay = 0; distance = 0; mode = 0
tempo = 0
note = 0
time_old = 0
current = None

delay_dic = {
    # mode =  4/4， 4/4,  3/4,  12/8
    120: [-1, 2000, 2000, 1500, 3000],
    90:  [-1, 2667, 2667, 2000, 4000],
    60:  [-1, 4000, 4000, 3000, 6000]
}

while True:
    # read datq from serial port
    # if run=0, will just wait until data is available
    data = ser.readline().decode().strip()

    # find the three integers in the string
    pattern = r'\d+'
    numbers = re.findall(pattern, data)
    [tempo, distance, mode] = [int(num) for num in numbers]

    if (tempo >= 120):
        tempo = 120
    elif (90 <= tempo < 120):
        tempo = 90
    else:
        tempo = 60

    delay = delay_dic[tempo][mode]

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