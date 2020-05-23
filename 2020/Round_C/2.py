
import sys
from collections import defaultdict


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def readinttab(n): return [readints() for _ in range(n)]


class CycleDetectedError(Exception):
    def __init__(self):
        super().__init__(self, "cycle detected")


def topological_sort_incoming_edges_iter(adj):
    """
    Iterative topological sort (incoming edges algorithm).
    Strict sort (if a -> b, then a < b), throws CycleDetectedError if
    there is a cycle.
    Complexity: O(|edges|)
    """
    parents = [0] * len(adj)
    for i, children in enumerate(adj):
        for j in children:
            parents[j] += 1

    candidates = [i for i, c in enumerate(parents) if c == 0]
    sort = []

    while candidates:
        node = candidates.pop()
        for child in adj[node]:
            parents[child] -= 1
            if parents[child] == 0:
                candidates.append(child)

        sort.append(node)

    if len(sort) != len(adj):
        raise CycleDetectedError()

    return sort


def to_num(x): return ord(x)-65


def to_chr(x): return chr(x+65)


T = readint()

for test in range(1, T+1):

    R, C = readints()

    wall = [list(readstr()) for _ in range(R)]

    possible = set()

    for w in wall:
        for b in w:
            possible.add(to_num(b))

    g = [set() for _ in range(26)]

    for w1, w2 in zip(wall, wall[1:]):
        for b1, b2 in zip(w1, w2):
            if b1 != b2:
                g[to_num(b2)].add(to_num(b1))

    g = [list(x) for x in g]

    # print(g)

    try:
        out = topological_sort_incoming_edges_iter(g)

        res = ""
        for x in out:
            if x in possible:
                res += to_chr(x)

        print("Case #{}: {}".format(test, res))

    except:

        print("Case #{}: {}".format(test, -1))
