import sys

N,M=map(int,sys.stdin.readline().split())
l=sorted(list(map(int,sys.stdin.readline().split())))
temp=[]
def dfs():
    if len(temp)==M:
        print(*temp)
        return
    for i in l:
        temp.append(i)
        dfs()
        temp.pop()
dfs()