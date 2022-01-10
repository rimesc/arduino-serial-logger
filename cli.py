import argparse
import os

from pathlib import Path

parser = argparse.ArgumentParser(description='Log serial data from Arduino board. If the name of a file is supplied '
                                             'then data is read from the file, rather than from the serial port')

parser.add_argument('file', type=Path, nargs='?', help='read CSV data from this file')
parser.add_argument('-o', '--output', metavar='<file>', dest='output_file', type=Path, help='write logged data to <file> as CSV')

args = parser.parse_args()

if args.file and not os.path.exists(args.file):
    parser.exit(1, 'No such file: {}\n'.format(str(args.file)))
if args.output_file and os.path.exists(args.output_file):
    parser.exit(1, 'File already exists: {}\n'.format(str(args.output_file)))
