
import sys


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


squares = {i*i for i in range(1000)}


def solve(arr, N):

    n = len(arr)

    cum_arr = [0]*(n+1)
    s = 0
    for i, x in enumerate(arr):
        cum_arr[i] = s
        s += x
    cum_arr[n] = s

    c = 0

    for i in range(N):
        for j in range(i+1, N+1):
            if cum_arr[j]-cum_arr[i] in squares:
                c += 1
    return c


T = readint()

for test in range(1, T+1):

    N = readint()
    arr = readints()

    print("Case #{}: {}".format(test, solve(arr, N)))
