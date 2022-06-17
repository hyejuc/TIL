import sys

N=int(sys.stdin.readline())
dp=[[1,1,1,1,1,1,1,1,1,1]]+[[0,0,0,0,0,0,0,0,0,0] for i in range(N-1)]
for i in range(1,N):
    for j in range(1,10):
        dp[i][j]=sum(dp[i-1][j:])%10007
res=0
for i in range(N):
    res+=sum(dp[i])%10007
print(res%10007)