import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
dp=[0]*N
for i in range(N):
    for j in range(i):
        if A[j]<A[i] and dp[j]>dp[i]:
            dp[i]=dp[j]
    dp[i]+=1
print(max(dp))