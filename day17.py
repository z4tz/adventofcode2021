import os
from inputreader import aocinput
from typing import List
from collections import namedtuple
import re
import math


def sumMToN(m: int, n: int) -> int:
    return int((abs(m-n)+1) * (m + n) / 2)


def invertsum1ToN(num: int) -> float:
    return (-1 + math.sqrt(1+8*num))/2


def maxHeight(data: List[str]) -> int:
    ymin = int(data[0].split('=')[-1].split('..')[0])
    return sumMToN(1, abs(ymin)-1)


def allVelocities(data: List[str]) -> int:
    Target = namedtuple('Target', 'xmin xmax ymin ymax')
    match = re.match(r'target area: x=([\d-]+)..([\d-]+), y=([\d-]+)..([\d-]+)', data[0])
    target = Target(*[int(group) for group in match.groups()])
    vxmin = math.ceil(invertsum1ToN(target.xmin))
    vxmax = target.xmax
    vymin = target.ymin
    vymax = target.ymax

    # for each timestep?
    for vx in range(vxmin, vxmax + 1):
        for vy in range(vymin, vymax + 1):
            pass


def main(day):
    data = aocinput(day)
    result = maxHeight(data)
    result2 = allVelocities(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
