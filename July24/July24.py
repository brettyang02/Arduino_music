import serial
import re
import time

ser = serial.Serial('COM3', 9600)

delay = 0
distance = 0
mode = 0
data_old = ""
note = 0


while True:
    data = ser.readline().decode().strip()
    
    '''
    if data != data_old:
        print("changed: " + data)
        data_old = data
    '''

    # find the three integers in the string
    pattern = r'\d+'
    numbers = re.findall(pattern, data)
    [delay, distance, mode] = [int(num) for num in numbers]
    print(delay, distance, mode)

    # turn distance to a note
    note = distance // 10
    if note > 7:
        note = 7


    print(note)
    time.sleep(delay / 1000)