def solve():
    n = int(input())
    x_tot, y_tot, z_tot = 0, 0, 0
    for _ in range(n):
        x, y, z = map(int, input().split(' '))
        x_tot += x; y_tot += y; z_tot += z
    print("YES") if x_tot == y_tot == z_tot == 0 else print("NO")


if __name__ == "__main__":
    solve()