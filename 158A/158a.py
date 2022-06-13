def solve():
    n, k = map(int, input().split(" "))
    res = 0
    nums = list(map(int, input().split(" ")))
    for i in range(len(nums)):
        if i+1 == k:
            # Add now then correct
            res += i
            j = i
            while (j < n and nums[j] > 0 and nums[j] == nums[i]): res += 1; j += 1 
            j = i - 1
            while (j >= 0 and nums[j] <= 0): res -=1; j -= 1
    print(res)



if __name__ == "__main__":
    solve()