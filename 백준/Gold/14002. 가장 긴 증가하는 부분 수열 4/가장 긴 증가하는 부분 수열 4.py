import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
dp=[0]*N
for i in range(N):
    for j in range(i):
        if A[i]>A[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
res=[]
a=max(dp)
for i in range(len(dp)-1,-1,-1):
    if dp[i]==a:
        res.append(A[i])
        a-=1
print(max(dp))
print(*reversed(res))