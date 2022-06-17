import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
dp=[1]
for i in range(1,N):
    temp=[]
    for j in range(i-1,-1,-1):
        if A[j]>A[i]:
            temp.append(dp[j])
    if not temp:
        dp.append(1)
    else:
        dp.append(max(temp)+1)
print(max(dp))