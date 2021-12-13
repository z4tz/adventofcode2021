import os
from inputreader import aocinput
from typing import List
import numpy as np


def printPaper(coordinates: List[List[int]]) -> None:
    np.set_printoptions(linewidth=200)
    xmax = max([val[0] for val in coordinates])
    ymax = max([val[1] for val in coordinates])
    paper = np.full((ymax+1, xmax+1), ' ')
    for x, y in coordinates:
        paper[y, x] = u"\u2588"
    print(np.array2string(paper, separator='', formatter={'str_kind': lambda val: val}))


def foldedPaper(data: List[str], visualization: bool = False) -> [int, str]:
    folds = []
    coordinates = []
    for line in data:
        if line.startswith('fold'):
            folds.append(line.strip())
        elif not line.isspace():  # skip empty lines
            coordinates.append(list(map(int, line.strip().split(','))))
    part1 = 0
    for j, fold in enumerate(folds):
        parts = fold.split(' ')[-1].split('=')
        axis = 1 if parts[0] == 'y' else 0
        foldAlong = int(parts[1])
        for i, coord in enumerate(coordinates):
            if coord[axis] > foldAlong:
                coord[axis] = coord[axis] - (coord[axis] - foldAlong) * 2
        if j == 0:
            part1 = len(set([tuple(coord) for coord in coordinates]))  # find unique elements
    if visualization:
        printPaper(coordinates)
    return part1, ""if visualization else "Enable visualization to show part 2 answer"


def main(day, visualization=False):
    data = aocinput(day)
    result = foldedPaper(data, visualization)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]), True)
