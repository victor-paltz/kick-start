
import sys

import math


class Fenwick:
    def __init__(self, l):
        self.l = [0] * (len(l) + 1)
        for i, x in enumerate(l):
            self.add(i, x)

    def add(self, i, x):
        # l[i] += x
        #assert 0 <= i < len(self.l) - 1
        i += 1
        while i < len(self.l):
            self.l[i] += x
            i += i & -i

    def set(self, i, x):
        self.add(i, x-self.sum_range(i, i+1))

    def sum(self, i):
        # sum(l[:i])
        #assert 0 <= i < len(self.l)
        s = 0
        while i > 0:
            s += self.l[i]
            i -= i & -i
        return s

    def sum_range(self, i, j):
        # sum(l[i:j])
        #assert 0 <= i <= j < len(self.l)
        return self.sum(j) - self.sum(i)


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


T = readint()

for test in range(1, T+1):

    N, Q = readints()

    tab = readints()

    s1 = Fenwick([x if i % 2 == 0 else -x for i, x in enumerate(tab)])

    s2 = Fenwick([x*(i+1) if i % 2 == 0 else -x*(i+1)
                  for i, x in enumerate(tab)])

    total = 0

    for _ in range(Q):

        query = readstr().split()

        if query[0] == "U":
            xj, vj = int(query[1]), int(query[2])
            xj -= 1
            s1.set(xj, vj if xj % 2 == 0 else -vj)
            s2.set(xj, vj*(xj+1) if xj % 2 == 0 else -vj*(xj+1))
        elif query[0] == "Q":
            Lj, Rj = int(query[1]), int(query[2])
            Lj -= 1
            Rj -= 1
            if Lj % 2 == 0:
                res = s2.sum_range(Lj, Rj+1) - Lj*s1.sum_range(Lj, Rj+1)
            else:
                res = -s2.sum_range(Lj, Rj+1) + Lj*s1.sum_range(Lj, Rj+1)

            total += res

    print("Case #{}: {}".format(test, total))
