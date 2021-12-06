import os
from inputreader import aocinput
from typing import List


def fishCounting(data: List[str], days) -> int:
    daysToBreeding = [0] * 9
    for time in data[0].split(','):
        daysToBreeding[int(time)] += 1
    for _ in range(days):
        newDaysToBreeding = [0] * 9
        newDaysToBreeding[6] = daysToBreeding[0]  # fishes that just bred
        newDaysToBreeding[8] = daysToBreeding[0]  # newborn fishes
        for i in range(8):  # move other fishes one day along
            newDaysToBreeding[i] += daysToBreeding[i+1]
        daysToBreeding = newDaysToBreeding
    return sum(daysToBreeding)


def main(day):
    data = aocinput(day)
    result = fishCounting(data, 80)
    result2 = fishCounting(data, 256)
    print(result, result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
