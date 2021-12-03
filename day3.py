import os
from inputreader import aocinput
from typing import List, Callable


def mostCommon(data: List[List[bool]]) -> List[bool]:
    summation = [0] * (len(data[0]))
    for line in data:
        for i, value in enumerate(line):
            summation[i] += value
    return [value >= len(data) / 2 for value in summation]


def leastCommon(data: List[List[bool]]) -> List[bool]:
    return [not value for value in mostCommon(data)]


def toInt(value: List[bool]) -> int:
    return int(''.join(map(str, map(int, value))), 2)


def listFilter(values: List[List[bool]], filtermethod: Callable[[List[List[bool]]], List[bool]]) -> List[bool]:
    index = 0
    while len(values) > 1:
        filtered = []
        filterValue = filtermethod(values)[index]
        for value in values:
            if value[index] == filterValue:
                filtered.append(value)
        values = filtered
        index += 1
    return values[0]


def powerConsumption(data: List[List[bool]]) -> [int, int]:
    gammarate = mostCommon(data)
    epsilonrate = [not value for value in gammarate]

    oxygenrating = listFilter(data.copy(), mostCommon)
    scrubberrating = listFilter(data.copy(), leastCommon)

    return toInt(gammarate) * toInt(epsilonrate), toInt(oxygenrating) * toInt(scrubberrating)


def main(day):
    data = aocinput(day)
    data = [[value == '1' for value in line.strip()] for line in data]
    result = powerConsumption(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
