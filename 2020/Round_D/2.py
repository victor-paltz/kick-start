
import sys


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


T = readint()

for test in range(1, T+1):

    k = readint()
    tab = readints()

    best = [0]*4
    prev = tab[0]

    for a in tab[1:]:

        if a == prev:
            continue

        b = best[:]

        if a > prev:
            best[0] = min(b[0]+1, b[1]+1, b[2]+1, b[3]+1)
            best[1] = min(b[0]+0, b[1]+1, b[2]+1, b[3]+1)
            best[2] = min(b[0]+0, b[1]+0, b[2]+1, b[3]+1)
            best[3] = min(b[0]+0, b[1]+0, b[2]+0, b[3]+1)
        else:
            best[0] = min(b[0]+1, b[1]+0, b[2]+0, b[3]+0)
            best[1] = min(b[0]+1, b[1]+1, b[2]+0, b[3]+0)
            best[2] = min(b[0]+1, b[1]+1, b[2]+1, b[3]+0)
            best[3] = min(b[0]+1, b[1]+1, b[2]+1, b[3]+1)

        prev = a

    print("Case #{}: {}".format(test, min(best)))
