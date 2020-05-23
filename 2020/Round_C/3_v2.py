
import sys
import numba as nb
import numpy as np
from math import sqrt


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


@nb.jit()
def is_square(x):
    d = round(sqrt(abs(x)))
    return d*d == x


@nb.jit()
def solve(cum_arr, N):
    c = 0
    i = 0
    j = 0
    while i < N:
        j = i+1
        while j < N+1:
            if is_square(cum_arr[j]-cum_arr[i]):
                c += 1
            j += 1
        i += 1
    return c


T = readint()
z = np.zeros((1,))

for test in range(1, T+1):

    N = readint()
    arr = np.array(readints(), dtype=int)

    cum_arr = np.cumsum(np.concatenate((z, arr)))

    print("Case #{}: {}".format(test, solve(cum_arr, N)))
