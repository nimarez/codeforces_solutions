import math

def solve():
    k, n, w = map(int, input().split(" "))
    print(max(0, math.ceil(0.5 * (w * (w+1)) * k - n)))


if __name__ == "__main__":
    solve()