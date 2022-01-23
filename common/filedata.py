import csv

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


class FileData:
    def __init__(self, reader):
        self.__reader = reader

    def read(self) -> Iterator[list[float]]:
        for data in self.__reader:
            yield data


@contextmanager
def file_data(file: Path) -> Iterator[FileData]:
    f = open(file, "r")
    try:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        yield FileData(reader)
    finally:
        f.close()
