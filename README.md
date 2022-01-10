# serial_logger

A toy Python project that reads data from an Arduino board over the serial port, plots it on screen in real-time and writes it to a CSV file for future analysis.

## Usage

```commandline
python3 logger.py 
```

### Notes

On MacOS, depending on the environment, it may be necessary to unset `DYLD_LIBRARY_PATH` (or set it to an empty string) before running, to work around an `ImportError` in `numpy`.