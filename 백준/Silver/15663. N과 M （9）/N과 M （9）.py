import sys

N,M=map(int,sys.stdin.readline().split())
l=sorted(list(map(int,sys.stdin.readline().split())))
v=[False]*N
temp=[]
def dfs():
    if len(temp)==M:
        print(*temp)
        return
    r=0
    for i in range(N):
        if not v[i] and r!=l[i]:
            v[i]=True
            temp.append(l[i])
            r=l[i]
            dfs()
            temp.pop()
            v[i]=False
dfs()