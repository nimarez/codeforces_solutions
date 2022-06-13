def solve():
    n = int(input())
    matrix = []
    zi, zj, has_zero = None, None, False
    
    for i in range(n):
        row = map(int, input().split(" "))
        factors = []
        for j, num in enumerate(row):
            twos, fives, temp = 0, 0, num
            if num == 0:
                zi, zj = i, j, True
            else:
                while(temp % 2 == 0): twos += 1; temp /= 2
                temp = num
                while(temp % 5 == 0): fives += 1; temp /= 5
        
            factors.append((twos, fives))
        matrix.append(factors)

    dp = [[[0, 0]] * (n+1) for _ in range(n+1)]
    for i in range(n):
        dp[i][n][0] = dp[n][i][0] = dp[i][n][1] = dp[n][i][1] = float('inf')

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            # TODO: what is wrong here?
            dp[i][j][0] = 0 if i == n-1 and j == n-1 else min(dp[i+1][j][0], dp[i][j+1][0]) + matrix[i][j][0]
            dp[i][j][1] = 0 if i == n-1 and j == n-1 else min(dp[i+1][j][1], dp[i][j+1][1]) + matrix[i][j][1]
    
    ans, arg = None, None
    if dp[n][n][0] < dp[n][n][1]:
        ans = dp[n][n][0]
        arg = 0
    else:
        ans = dp[n][n][1]
        arg = 1


    path = []
    if (has_zero and ans > 1):
        # zero is better
        for i in range(zi):
            path.append('R')
        for j in range(zj):
            path.append('D')
        
        for i in range(zi, n-1):
            path.append('R')
        for j in range(zj, n-1):
            path.append('D')
        
        print(1)
        print("".join(path))
    else:
        # dp path is better
        i, j = 0, 0
        while(i != n-1 or j != n-1):
            if(i < n-1 and dp[i][j][arg] == matrix[i][j][arg] + dp[i+1][j][arg]):
                path.append('D')
                i += 1
            elif(j < n-1):
                path.append('R')
                j += 1
        print(ans)
        print("".join(path))

    


    

        
        


            

if __name__ == "__main__":
    solve()