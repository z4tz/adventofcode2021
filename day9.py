import os
from inputreader import aocinput
from typing import List, Union
import numpy as np
from collections import deque


def findArea(heightmap: np.ndarray, start: Union) -> int:
    visited = set()
    tovisit = deque([start])
    while tovisit:
        x, y = tovisit.pop()
        for ix, iy in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
            if heightmap[iy, ix] < 9 and (ix, iy) not in visited:
                tovisit.append((ix, iy))
        visited.add((x, y))
        heightmap[y, x] = 9  # set height to 9 to not start area here again
    return len(visited)


def lowPoints(data: List[str]) -> [int, int]:
    heightmap = np.array([[int(number) for number in line.strip()] for line in data])
    heightmap = np.pad(heightmap, 1, 'maximum')  # padding to avoid "fetching values outside array"
    risksum = 0
    areasizes = []
    for iy in range(1, heightmap.shape[0]-1):
        for ix in range(1, heightmap.shape[1]-1):
            if heightmap[iy, ix] < min([heightmap[iy, ix-1], heightmap[iy, ix+1], heightmap[iy-1, ix], heightmap[iy+1, ix]]):
                risksum += heightmap[iy, ix] + 1

    for iy in range(1, heightmap.shape[0]-1):
        for ix in range(1, heightmap.shape[1]-1):
            if heightmap[iy, ix] < 9:
                areasizes.append(findArea(heightmap, (ix, iy)))
    return risksum, np.prod(sorted(areasizes)[-3:])


def main(day):
    data = aocinput(day)
    result = lowPoints(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
