
import sys


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


T = readint()

for test in range(1, T+1):

    N, K = readints()

    tab = readints()

    #match = list(reversed(range(1, K+1)))

    c = 0
    start = False
    prev = -1

    # print(tab)

    for i, v in enumerate(tab):
        if start and (prev == v):
            if v == 1:
                c += 1
                start = False
                continue
            else:
                prev -= 1
                continue
        elif v == K:
            start = True
            prev = v-1
        else:
            start = False

    print("Case #{}: {}".format(test, c))
