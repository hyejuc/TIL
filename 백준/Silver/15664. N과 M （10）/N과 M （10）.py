import sys

N,M=map(int,sys.stdin.readline().split())
l=sorted(list(map(int,sys.stdin.readline().split())))
temp=[]
def dfs(start):
    if len(temp)==M:
        print(*temp)
        return
    r=0
    for i in range(start,N):
        if r!=l[i]:
            temp.append(l[i])
            r=l[i]
            dfs(i+1)
            temp.pop()
dfs(0)