# Implementation took 5m49s (looking at problem not included)
def solve():
    for i in range(5):
        for j, num in enumerate(map(int, input().split(" "))):
            if num == 1:
                print(abs(i-2) + abs(j-2))
                return


if __name__ == "__main__":
    solve()