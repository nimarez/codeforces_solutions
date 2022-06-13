# Entire process (ideation + imp) took 3m56s (that's kinda a lot for this problem lol)
def solve():
    f, s = input().lower(), input().lower()
    # hand implementation
    for u, v in zip(f, s):
        if u < v: # even this can be made into ord(u) < ord(v) if we're going *really* hand
            print(-1)
            return
        elif u > v:
            print(1)
            return
    print(0)
    return


    # using python's native features
    if f < s: print(-1)
    elif f > s: print(1)
    else: print(0)



if __name__ == "__main__":
    solve()
    




