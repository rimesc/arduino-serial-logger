import serial

from contextlib import contextmanager
from typing import Iterator


class SerialData:
    def __init__(self, ser):
        self.__ser = ser

    def read(self) -> Iterator[list[float]]:
        while True:
            try:
                data = self.__readline()
                if len(data) > 0:
                    yield data
            except:
                break

    # Read a line from the serial port and parse it as comma-separated floating-point values
    def __readline(self) -> list[float]:
        bytes = self.__ser.readline().decode('utf-8')
        if bytes.startswith('MPU6050'):
            return []
        return [float(v) for v in bytes.split(',')]


@contextmanager
def serial_data() -> Iterator[SerialData]:
    ser = serial.Serial('/dev/tty.usbmodem00001')
    ser.flushInput()
    try:
        yield SerialData(ser)
    finally:
        ser.close()
