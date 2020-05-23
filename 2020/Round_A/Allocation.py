
import sys


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


T = readint()

for test in range(1, T+1):

    N, B = readints()
    tab = readints()
    tab.sort()

    for i, p in enumerate(tab):
        if p > B:
            i -= 1
            break
        B -= p

    print("Case #{}: {}".format(test, i+1))
