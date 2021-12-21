import os
from inputreader import aocinput
from typing import List, Union
from itertools import permutations


class Pair:
    def __init__(self, element: Union[List, int, 'Pair'], parent: Union['Pair', None] = None):
        if type(element[0]) is list:
            self.left = Pair(element[0], self)
        else:  # if int or Pair
            self.left = element[0]
            if type(self.left) is Pair:
                self.left.parent = self
        if type(element[1]) is list:
            self.right = Pair(element[1], self)
        else:  # if int or Pair
            self.right = element[1]
            if type(self.right) is Pair:
                self.right.parent = self
        self.parent = parent

    def __repr__(self):
        return f'[{self.left}, {self.right}]'


def split(pair: Pair, side: str):
    if side == 'left':
        value = pair.left
        pair.left = Pair([value//2, value//2 + value % 2], pair)
    else:
        value = pair.right
        pair.right = Pair([value // 2, value // 2 + value % 2], pair)


def explode(pair: Pair):
    parent = pair.parent
    addLeft(pair.left, pair)
    addRight(pair.right, pair)
    if parent.left == pair:
        parent.left = 0
    else:
        parent.right = 0


def addLeft(value: int, child: Pair):
    current = child.parent
    while type(current) is Pair and current.left == child:  # find first time child is not on the left
        child = current
        current = child.parent
        if current is None:  # if child is left for each branch
            return
    if type(current.left) is int:
        current.left += value
    else:
        current = current.left
        while type(current.right) is Pair:  # climb tree until integer is found
            current = current.right
        current.right += value


def addRight(value: int, child: Pair):
    current = child.parent
    while type(current) is Pair and current.right == child:  # find first time child is not on the left
        child = current
        current = child.parent
        if current is None:  # if child is left for each branch
            return
    if type(current.right) is int:
        current.right += value
    else:
        current = current.right
        while type(current.left) is Pair:  # climb tree until integer is found
            current = current.left
        current.left += value


def findExplosion(pair: Pair, nestedlevel: int = 0):
    if nestedlevel == 4:
        explode(pair)
        return True

    for child in [pair.left, pair.right]:
        if type(child) is Pair and findExplosion(child, nestedlevel+1):
            return True
    return False


def findSplit(pair):
    if type(pair.left) is Pair:
        if findSplit(pair.left):
            return True
    elif pair.left >= 10:
        split(pair, 'left')
        return True
    if type(pair.right) is Pair:
        if findSplit(pair.right):
            return True
    elif pair.right >= 10:
        split(pair, 'right')
        return True
    return False  # if no split is found


def reduce(pair: Pair):
    while True:
        if not findExplosion(pair):
            if not findSplit(pair):
                return pair


def calcMagnitude(pair: Union[Pair, int]) -> int:
    if type(pair) is int:
        return pair
    return calcMagnitude(pair.left)*3 + calcMagnitude(pair.right)*2


def magnitudeOfSum(data: List[str]) -> [int, int]:
    snailnumbers = [Pair(eval(line.strip())) for line in data]
    total = snailnumbers[0]
    for snailnumber in snailnumbers[1:]:
        total = Pair([total, snailnumber])
        reduce(total)

    maxMagnitude = 0
    for a, b in permutations([eval(line.strip()) for line in data], 2):
        magnitude = calcMagnitude(reduce(Pair([a, b])))
        if magnitude > maxMagnitude:
            maxMagnitude = magnitude
    return calcMagnitude(total), maxMagnitude


def main(day):
    data = aocinput(day)
    result = magnitudeOfSum(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
