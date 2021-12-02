import os
from inputreader import aocinput


def main(day):
    data = aocinput(day)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
