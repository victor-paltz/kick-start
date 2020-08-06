
import sys


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


T = readint()

for test in range(1, T+1):

    n = readint()
    v = readints()

    s = 0
    maxi = -1
    for x, y in zip(v, v[1:]):
        if x > maxi and x > y:
            s += 1
        maxi = max(maxi, x)
    if v[-1] > maxi:
        s += 1

    print("Case #{}: {}".format(test, s))
