for tc in range(int(input())):
    n, k = map(int, input().split())
    data = [input() for x in range(n)]
    dp = [[[[0]*(k+1),[0]*(k+1)] for x in range(n)] for y in range(n)]
    if data[0][1] != 'H':
        dp[0][1][1][-1] = 1
    if data[1][0] != 'H':
        dp[1][0][0][-1] = 1
    for diag in range(2, 2*n-1):
        for i in range(diag+1):
            if i>=n:
                break
            j = diag-i
            if j>=n or data[i][j]=='H':
                continue
            left = [[0]*(k+1),[0]*(k+1)]
            if i:
                left = dp[i-1][j]
            up = [[0]*(k+1),[0]*(k+1)]
            if j:
                up = dp[i][j-1]
            for reduction in range(k):
                dp[i][j][0][reduction] += left[0][reduction]+left[1][reduction+1]
                dp[i][j][1][reduction] += up[1][reduction]+up[0][reduction+1]
            dp[i][j][0][-1] += left[0][-1]
            dp[i][j][1][-1] += up[1][-1]
    print(sum(dp[-1][-1][0])+sum(dp[-1][-1][1]))
