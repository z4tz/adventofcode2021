import os
from inputreader import aocinput
from typing import List
import numpy as np


def flashingOctopuses(data: List[str]) -> [int, int]:
    octopuses = np.array([[int(number) for number in line.strip()] for line in data])
    octopuses = np.pad(octopuses, 1, 'constant')
    flashes = 0

    def isPadding(x, y):
        return x <= 0 or x >= octopuses.shape[0]-1 or y <= 0 or y >= octopuses.shape[1]-1

    def flash(x: int, y: int):
        octopuses[y - 1:y + 2, x - 1:x + 2] += 1
        for jy in range(y - 1, y + 2):
            for jx in range(x - 1, x + 2):
                if octopuses[jy, jx] > 9 and (jx, jy) not in flashed and not isPadding(jx, jy):
                    flashed.add((jx, jy))
                    flash(jx, jy)
    steps = 0
    while np.sum(octopuses[1:-1, 1:-1]):
        octopuses += 1
        flashed = set()
        for iy in range(1, octopuses.shape[0]-1):
            for ix in range(1, octopuses.shape[1]-1):
                if octopuses[iy, ix] > 9 and (ix, iy) not in flashed:
                    flashed.add((ix, iy))
                    flash(ix, iy)

        octopuses[octopuses > 9] = 0
        flashes += len(flashed)
        steps += 1
        if steps == 100:
            part1 = flashes
    return part1, steps




def main(day):
    data = aocinput(day)
    result = flashingOctopuses(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
