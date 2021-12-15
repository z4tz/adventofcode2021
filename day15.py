import os
import queue
from inputreader import aocinput
from typing import List
import numpy as np


def dijkstra(costmap: np.ndarray, start: [int, int], goal: [int, int]) -> int:
    tovisit = queue.PriorityQueue()
    tovisit.put((0, start))

    def getNeighbors(p: [int, int]) -> List[tuple[int, int]]:
        validneighbors = []
        xmax, ymax = costmap.shape
        for x, y in [(p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)]:
            if 0 <= x < xmax and 0 <= y < ymax:
                validneighbors.append((x, y))
        return validneighbors

    lowestCost = {start: 0}
    while True:
        current = tovisit.get()[1]
        if current == goal:
            break
        for neighbor in getNeighbors(current):
            neighborCost = lowestCost[current] + costmap[neighbor[1], neighbor[0]]
            if neighbor not in lowestCost or lowestCost[neighbor] > neighborCost:
                lowestCost[neighbor] = neighborCost
                tovisit.put((neighborCost, neighbor))
    return lowestCost[goal]


def expandMap(riskmap: np.ndarray) -> np.ndarray:
    width = riskmap.shape[0]
    height = riskmap.shape[1]
    largemap = np.empty((width * 5, height * 5))
    for y in range(5):
        for x in range(5):
            largemap[height * y:height * y + height, width * x:width * x + width] = riskmap + (y + x)
    return np.subtract(largemap, (largemap > 9) * 9)


def safestPath(data: List[str]) -> [int, int]:
    riskmap = np.array([[int(number) for number in line.strip()] for line in data])
    largemap = expandMap(riskmap)
    start = (0, 0)
    goal = (riskmap.shape[0] - 1, riskmap.shape[1] - 1)
    goal2 = (largemap.shape[0] - 1, largemap.shape[1] - 1)
    result = dijkstra(riskmap, start, goal)
    result2 = dijkstra(largemap, start, goal2)
    return result, result2


def main(day):
    data = aocinput(day)
    result = safestPath(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
