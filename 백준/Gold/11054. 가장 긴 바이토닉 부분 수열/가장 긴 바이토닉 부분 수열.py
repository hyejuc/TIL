import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
dp=[1]
for i in range(1,N):
    temp=[]
    for j in range(i):
        if A[j]<A[i]:
            temp.append(dp[j])
    if not temp:
        dp.append(1)
    else:
        dp.append(max(temp)+1)
dp2=[0]*N
for i in range(N-1,-1,-1):
    temp2=[]
    for j in range(N-1,i,-1):
        if A[i]>A[j]:
            temp2.append(dp2[j])
    if not temp2:
        dp2[i]=1
    else:
        dp2[i]=max(temp2)+1
DP=[x+y-1 for x,y in zip(dp,dp2)]
print(max(DP))