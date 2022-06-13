# Naive solution, failed. AC needs to use 2s and 5s

# Look at this beautiful solution: https://codeforces.com/contest/2/submission/62187713
def solve():
    n = int(input())
    matrix = [[] for _ in range(n)]
    for i in range(n):
        for m in input().split(" "):
            matrix[i].append(int(m))
 
    dp = [[(1, '')] * n for _ in range(n)]
    dp[0][0] = (matrix[0][0], '')
    
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            RN = dp[i][j-1][0] * matrix[i][j] if j-1 >= 0 else float('inf')
            DN = dp[i-1][j][0] * matrix[i][j] if i-1 >= 0 else float('inf')

            if zeros(RN) <= zeros(DN):
                dp[i][j] = (RN, dp[i][j-1][1] + 'R')
            else:
                dp[i][j] = (DN, dp[i-1][j][1] + 'D')  

    return zeros(dp[n-1][n-1][0]), dp[n-1][n-1][1]

def zeros(num):
    if num == float('inf'):
        return float('inf')
    z = 0
    while(num % 10 == 0):
        z += 1
        num = num // 10     
    return z

def path_values(matrix, path):
    print(path)
    n = len(matrix)
    res = [[1] * n for _ in range(n)]
    value, res[0][0] = matrix[0][0], matrix[0][0]
    i, j = 0, 0
    for p in path:
        if p == 'D':
            i += 1
            value *= matrix[i][j]
            res[i][j] = value
        elif p == 'R':
            j += 1
            value *= matrix[i][j]
            res[i][j] = value
    return res



def tests():
    assert zeros(3000) == 3
    assert zeros(234345) == 0
    assert zeros(1230) == 1
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def pretty_print(arr):
    for row in arr:
        print(row)
    print()

if __name__ == "__main__":
    tests()
    zeros, way = solve()
    print(zeros)
    print(way)