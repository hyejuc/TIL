import sys

N,M=map(int,sys.stdin.readline().split())
temp=[]
def dfs(start):
    if len(temp)==M:
        print(*temp)
        return
    for i in range(start,N+1):
        temp.append(i)
        dfs(i)
        temp.pop()
dfs(1)