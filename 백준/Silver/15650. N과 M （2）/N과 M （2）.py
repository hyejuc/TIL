import sys

N,M=map(int,sys.stdin.readline().split())
temp=[]
def dfs(x):
    if len(temp)==M:
        print(*temp)
        return
    for i in range(x,N+1):
        if i not in temp:
            temp.append(i)
            dfs(i+1)
            temp.pop()
dfs(1)
