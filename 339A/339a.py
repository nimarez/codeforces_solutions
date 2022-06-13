def solve():
    nums = list(map(int, input().split("+")))
    nums.sort()
    print("+".join(map(str, nums)))


if __name__ == "__main__":
    solve()