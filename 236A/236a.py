def solve():
    s = input()
    print("CHAT WITH HER!") if len(set(s)) % 2 == 0 else print("IGNORE HIM!")


if __name__ == "__main__":
    solve()