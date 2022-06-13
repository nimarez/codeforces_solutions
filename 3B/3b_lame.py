def solve():
    n, v = map(int, input().split(" "))
    ones, twos = [], []
    for i in range(n):
        ti, pi = map(int, input().split(" "))
        if ti == 1: ones.append((i+1, pi))
        else: twos.append((i+1, pi))
    
    # sort but keep original indices
    ones = sorted(ones, key=lambda x: x[1], reverse=True)
    twos = sorted(twos, key=lambda x: x[1], reverse=True)
   
    # breakpoint()
    total, res = 0, []
    while (v > 3 and len(ones) >= 2 and len(twos) >= 1):
        if sum_num(ones[:2]) >= twos[0][1]:
            total += sum_num(ones[:2])
            res.extend([ones[0][0], ones[1][0]])
            del ones[:2]
        else:
            total += twos[0][1]
            res.append(twos[0][0])
            del twos[0]
        v -= 2
        
    if v > 0:
        if len(twos) == 0:
            total += sum_num(ones[:v])
            for i in range(v): res.append(ones[i][0])
        elif len(ones) == 0:
            total += sum_num(twos[:(v // 2)])
            for i in range(v // 2): res.append(twos[i][0])
        else:
            # len ones == 1, len twos can be anything
            if v % 2 == 1:
                total += sum_num(twos[:(v // 2)])
                for i in range(v // 2): res.append(twos[i][0])
                total += ones[0][1]
                res.append(ones[0][0])
            else:
                last_two = v // 2 - 1
                for i in range(last_two): res.append(twos[i][0])
                total += sum_num(twos[:(last_two)])
                
                if ones[0][1] >= twos[last_two][1]:
                    total += ones[0][1]
                    res.append(ones[0][0])
                else:
                    total += twos[last_two][1]
                    res.append(twos[last_two][0])
    return total, res
                    


def sum_num(arr):
    res = 0
    for _, num in arr:
        res += num
    return res




if __name__ == "__main__":
    total, res = solve()
    print(total)
    print(" ".join(map(str, res)))