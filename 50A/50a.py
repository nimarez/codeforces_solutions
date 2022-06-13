def solve():
    m, n = map(int, input().split(" "))
    mm, rm = m // 2, m % 2
    nn, rn = n // 2, n % 2
    res = 0

    if rm * m == rn * n:
        # both even or both the same number
        res += (m * n) // 2
    else:
        res += nn * m # row by row lay out the dominos
        if rn == 1: # if one column left
            res += mm 
      
    print(res)


            


if __name__ == "__main__":
    solve()