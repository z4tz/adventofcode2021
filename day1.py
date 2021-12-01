from inputreader import aocinput
from typing import List


def depthincreases(depths: List[int], offset: int = 1) -> int:
    return sum([depths[i] < depths[i + offset] for i in range(len(depths) - offset)])


def main(day: int):
    data = aocinput(day)
    data = [int(line) for line in data]
    print(depthincreases(data))
    print(depthincreases(data, 3))


if __name__ == '__main__':
    main(int(__file__.split('/')[-1][3:-3]))
