import sys

N,M=map(int,sys.stdin.readline().split())
temp=[]
def dfs():
    if len(temp)==M:
        print(*temp)
        return
    for i in range(1,N+1):
        if i not in temp:
            temp.append(i)
            dfs()
            temp.pop()
dfs()