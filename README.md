# Arduino serial logger

Python code for reading data from an Arduino board over the serial port.  The data is plotted on screen in real-time and optionally written it to a CSV file for future analysis.

Inspired in part by [this blog post](https://makersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial).

## Usage

E.g.
```commandline
python3 -m move.demo4
```

### Notes

On MacOS, depending on the environment, it may be necessary to unset `DYLD_LIBRARY_PATH` (or set it to an empty string) before running, to work around an `ImportError` in `numpy`.
