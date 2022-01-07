import serial

ser = serial.Serial('/dev/tty.usbmodem00001')
ser.flushInput()


# Read a line from the serial port and parse it as comma-separated floating-point values
def __readline():
    try:
        bytes = ser.readline().decode('utf-8')
        if bytes.startswith('MPU6050'):
            return []
        return [float(v) for v in bytes.split(',')]
    except:
        return []


# Read data from the serial point
def read():
    while True:
        data = __readline()
        if len(data) > 0:
            yield data
