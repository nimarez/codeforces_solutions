def solve():
    n = int(input())
    res = 0
    for _ in range(n):
        s = sum(map(int, input().split(" ")))
        if s >= 2:
            res += 1
    print(res)
            

        

if __name__ == "__main__":
    solve()