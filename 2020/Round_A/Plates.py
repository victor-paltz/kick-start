
import sys
from functools import lru_cache


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


T = readint()

for test in range(1, T+1):

    N, K, P = readints()

    stacks = readinttab(N)

    @lru_cache(None)
    def get_best(p, i):

        if i < 0:
            return 0 if p == 0 else -float("inf")

        if p < 0:
            return -float("inf")

        if p == 0:
            return 0

        best = get_best(p, i-1)
        if stacks[i]:
            s = 0
            for k, x in enumerate(stacks[i]):
                s += x
                if p >= k-1:
                    best = max(best, s + get_best(p-k-1, i-1))

        return best

    sol = get_best(P, N-1)

    print("Case #{}: {}".format(test, sol))
