import os
from inputreader import aocinput
from typing import List, Callable


def fuelOptimization(data: List[str], fuelmethod: Callable[[int], int]) -> int:
    positions = [int(value) for value in data[0].split(',')]
    guess = int(sum(positions)/len(positions))
    guess1 = sum([fuelmethod(abs(position - guess)) for position in positions])
    guess2 = sum([fuelmethod(abs(position - guess + 1)) for position in positions])
    if guess1 < guess2:
        change = 1
        previousConsumtion = guess1
    else:
        change = -1
        previousConsumtion = guess2
    while True:
        guess += change
        consumption = sum([fuelmethod(abs(position - guess))for position in positions])
        if consumption > previousConsumtion:
            break
        else:
            previousConsumtion = consumption
    return previousConsumtion


def main(day):
    data = aocinput(day)
    result = fuelOptimization(data, lambda x: x)
    result2 = fuelOptimization(data, lambda x: int(x*(x+1)/2))
    print(result, result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
