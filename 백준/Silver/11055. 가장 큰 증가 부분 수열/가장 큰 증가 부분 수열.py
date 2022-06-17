import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
dp=[A[0]]
for i in range(1,N):
    temp=[]
    for j in range(i-1,-1,-1):
        if A[j]<A[i]:
            temp.append(dp[j])
    if not temp:
        dp.append(A[i])
    else:
        dp.append(A[i]+max(temp))
print(max(dp))