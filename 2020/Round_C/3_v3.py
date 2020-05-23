
import sys


def readstr(): return sys.stdin.readline().strip()


def readint(): return int(readstr())


def readints(): return [int(x) for x in readstr().split()]


def solve(arr, N):

    maxA = 100
    squares = [i*i for i in range(int((maxA*N)**.5)+2)]

    offset = 0
    s = 0
    for x in arr:
        s += x
        offset = min(offset, s)
    offset = -offset

    count_subsum = [0]*(N*maxA)
    count_subsum[0+offset] = 1

    tot = 0

    cum_sum = 0
    for x in arr:
        cum_sum += x
        for s in squares:
            if cum_sum-s+offset < 0:
                break
            tot += count_subsum[cum_sum-s+offset]
        count_subsum[cum_sum+offset] += 1

    return tot


T = readint()

for test in range(1, T+1):

    N = readint()
    arr = readints()

    print("Case #{}: {}".format(test, solve(arr, N)))
