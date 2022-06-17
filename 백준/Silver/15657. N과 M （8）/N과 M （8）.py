import sys

N,M=map(int,sys.stdin.readline().split())
l=sorted(list(map(int,sys.stdin.readline().split())))
temp=[]
def dfs(start):
    if len(temp)==M:
        print(*temp)
        return
    for i in range(start,len(l)):
        temp.append(l[i])
        dfs(i)
        temp.pop()
dfs(0)