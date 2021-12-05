import os
from inputreader import aocinput
from typing import List
from collections import defaultdict


def rangeSpecial(val1, val2):
    """Generator extending range. Yields each integer numbers between the given values, including endpoints"""
    if val1 < val2:
        for val in range(val1, val2+1):
            yield val
    else:
        for val in range(val1, val2 - 1, -1):
            yield val


def overlap(data: List[str], diagonal=False):
    points = defaultdict(int)
    for line in data:
        values = [int(value) for value in line.replace(' -> ', ',').split(',')]
        if values[0] == values[2]:
            for y in rangeSpecial(values[1], values[3]):
                points[(values[0], y)] += 1
        elif values[1] == values[3]:
            for x in rangeSpecial(values[0], values[2]):
                points[(x, values[1])] += 1
        elif diagonal:
            for x, y in zip(rangeSpecial(values[0], values[2]), rangeSpecial(values[1], values[3])):
                points[(x, y)] += 1
    return sum(value > 1 for value in points.values())


def main(day):
    data = aocinput(day)
    result = overlap(data)
    result2 = overlap(data, True)
    print(result, result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
