def solve():
    n = int(input())
    for _ in range(n):
        num = int(input())
        rightmost = num % 2
        ans = 1
        if (rightmost and num ^ ans > 0) or (not rightmost and num & ans > 0):
            print(ans)
        else:
            breakpoint()
            m = num // 2
            i = 1
            while not ((rightmost and num ^ ans > 0) or (not rightmost and num & ans > 0)):
                if 2*(m % 2)-1 == rightmost:
                    ans = ans + 2 ** i
                    break
                m = m // 2
                i += 1
            print(ans)
    return

if __name__ == "__main__":
    solve()