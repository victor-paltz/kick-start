
import sys


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


T = readint()

for test in range(1, T+1):

    N, K = readints()

    tab = readints()

    c = 0

    i = 0
    while i < len(tab)-K+1:
        if all(tab[i+k] == K-k for k in range(K)):
            c += 1
            i += K-1
        i += 1

    print("Case #{}: {}".format(test, c))
