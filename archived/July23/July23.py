import serial

# Replace 'COM3' with the appropriate serial port for your Arduino
ser = serial.Serial('COM3', 9600)

try:
    while True:
        # Read a line of data from the serial port
        data = ser.readline().decode().strip()
        
        # Check if there's valid data received
        if data:
            print(data)

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()