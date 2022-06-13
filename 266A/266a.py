def solve():
    n = int(input())
    s = input()
    curr, total = "", 0
    for c in s:
        if c == curr:
            total += 1
        curr = c
    print(total)



if __name__ == "__main__":
    solve()