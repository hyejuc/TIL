import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
if n==1:
    print(a[0])
else:
    dp = [[a[0]], [a[0]]]
    for i in range(1, n):
        dp[0].append(max(dp[0][i - 1] + a[i], a[i]))
        dp[1].append(max(dp[0][i - 1], dp[1][i - 1] + a[i]))
    print(max(max(dp[0]),max(dp[1])))