import os
from inputreader import aocinput
from typing import List, Set
from collections import defaultdict


def findPaths(data: List[str]) -> [int, int]:
    nodes = defaultdict(list)
    for line in data:
        location1, location2 = line.strip().split('-')
        nodes[location1].append(location2)
        nodes[location2].append(location1)

    paths = []
    paths2 = []

    def travel(current: str, visited: Set[str]):
        visited.add(current)
        if 'end' in current:
            paths.append(visited)
            return
        for destination in nodes[current]:
            if destination.isupper() or destination not in visited:
                travel(destination, visited.copy())

    def travel2(current: str, visited: Set[str], specialVisit: bool = False):
        if 'end' == current:
            paths2.append(visited)
            return
        visited.add(current)
        for destination in nodes[current]:
            if destination.isupper():
                travel2(destination, visited.copy(), specialVisit)
            elif destination not in visited:
                travel2(destination, visited.copy(), specialVisit)
            elif not specialVisit and 'start' != destination:
                travel2(destination, visited.copy(), True)

    travel('start', set())
    travel2('start', set())

    return len(paths), len(paths2)


def main(day):
    data = aocinput(day)
    result = findPaths(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
