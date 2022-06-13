import math


def solve():
    a, b = map(int, input().split(' '))
    print(math.floor(math.log(b/a, 3/2)) + 1)


if __name__ == "__main__":
    solve()