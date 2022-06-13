def solve():
    res, vowels = [], ['a', 'e', 'i', 'o', 'u', 'y']
    for c in input():
        if c.lower() not in vowels:
            res.append(f".{c.lower()}")
        
    print("".join(res))

if __name__ == "__main__":
    solve()