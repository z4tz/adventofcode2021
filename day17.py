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
    vymax = abs(target.ymin)

    initialVelocities = set()
    for step in range(max([vxmax, vymax*2+1])):
        xvels = []
        yvels = []
        for vx in range(vxmin, vxmax + 1):
            if step > vx:
                xpos = sumMToN(1, vx)
            else:
                xpos = sumMToN(vx-step, vx)
            if target.xmin <= xpos <= target.xmax:
                xvels.append(vx)
            if xpos > target.xmax:
                break

        for vy in range(vymin, vymax + 1):
            ypos = sumMToN(vy-step, vy)
            if target.ymin <= ypos <= target.ymax:
                yvels.append(vy)
            if ypos > target.ymax:
                break

        for yvel in yvels:
            for xvel in xvels:
                initialVelocities.add((xvel, yvel))

    return len(initialVelocities)


def main(day):
    data = aocinput(day)
    result = maxHeight(data)
    result2 = allVelocities(data)
    print(result, result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
