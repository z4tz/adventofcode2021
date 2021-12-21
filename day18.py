import os
from inputreader import aocinput
from typing import List, Union


class Pair:
    def __init__(self, element: Union[List, int], parent: Union['Pair', None]=None):
        if type(element[0]) is list:
            self.left = Pair(element[0], self)
        else:
            self.left = element[0]
        if type(element[1]) is list:
            self.right = Pair(element[1], self)
        else:
            self.right = element[1]
        self.parent = parent

    def __repr__(self):
        return f'[{self.left}, {self.right}]'


def explode(pair: Pair):
    parent = pair.parent
    if parent.left == pair:
        parent.left = 0

    else:
        parent.right = 0
    addLeft(pair.left, parent)
    addRight(pair.right, parent)


def addLeft(value: int, pair: Pair):
    pass


def addRight(value: int, pair: Pair):
    pass


def magnitudeOfSum(data: List[str]) -> int:
    snailnumbers = [Pair(eval(line.strip())) for line in data]
    print(snailnumbers)


def main(day):
    data = aocinput(day)
    result = magnitudeOfSum(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
