"""

PGM parsing library for CS674 (Image Processing) at UNR.

"""

from pathlib import Path
from typing import Dict, List


class InvalidPGMFormat(Exception):
    pass


def itobs(i: int) -> bytes:
    """ Convert integer to byte string. """
    return str(i).encode("ascii")


class PGMImage:
    signature: str
    cols: int
    rows: int
    quantization: int
    pixels: List[List[int]]
    comments: List[str]
    name: str

    def __init__(self, pgm_filename):
        """ Read a PGM file given its filename. """
        self.signature = None
        self.cols, self.rows, self.quantization = None, None, None
        self.pixels = []
        self.comments = []

        self.name = Path(pgm_filename).name

        with open(pgm_filename, "rb") as pgm_file:
            self.signature = pgm_file.read(2).decode("ascii")

            if self.signature != "P5":  # Other formats not used in CS674
                raise InvalidPGMFormat(
                    f"Format was {signature}, but only raw greyscale bytes"
                    " are acceptable."
                )

            while not (self.cols and self.rows and self.quantization):
                # Read .PGM header. This handles multiple, out-of-order
                # comments (preceded by '#'), and metadata (C, R, Q) in-order
                # but possibly seperated by line breaks.
                line = pgm_file.readline().decode("ascii")

                if line.startswith("#"):
                    self.comments.append(line)
                else:
                    line = line.strip().split()  # Strip trailing newlines

                    for num in line:
                        num = int(num)

                        if not self.cols:
                            self.cols = num
                        elif not self.rows:
                            self.rows = num
                        elif not self.quantization:
                            self.quantization = num

            # Read pixel contents given header parameters
            for i in range(self.rows):
                self.pixels.append(pgm_file.read(self.cols))

            if pgm_file.read() != b"":
                raise InvalidPGMFormat(
                    f"Finished reading {pgm_filename} but content still left."
                )

    @property
    def n_pixels(self) -> int:
        return self.rows * self.cols

    def save(self, pgm_filename):
        """ Write this PGM image to a file. """

        with open(pgm_filename, "wb") as f:
            lines = [
                b"P5\n",
                itobs(self.cols) + b" " + itobs(self.rows) + b"\n",
                itobs(self.quantization) + b"\n",
                *self.pixels,
            ]
            f.writelines(lines)

    def get_histogram(self, normed=False) -> List[int]:
        unrolled_pxls = []

        for row in self.pixels:
            for pxl in row:
                unrolled_pxls.append(int(pxl))

        histogram = [0] * self.quantization

        for pxl in unrolled_pxls:
            histogram[pxl] += 1

        if normed:
            for i in range(self.quantization):
                histogram[i] /= self.n_pixels

        return histogram

    def show_histogram(self, normed=False, title=None):
        import matplotlib.pyplot as plot

        # plot.ion()  # Don't block while showing the histogram

        unrolled_pxls = []

        for row in self.pixels:
            for pxl in row:
                unrolled_pxls.append(int(pxl))

        plot.hist(unrolled_pxls, bins=255, density=normed)

        plot.xlabel("Pixel Value")
        plot.ylabel("Count" if not normed else "Probability")

        if not title:
            title = f"Histogram of {self.name}"
        plot.title(title)

        plot.show()
