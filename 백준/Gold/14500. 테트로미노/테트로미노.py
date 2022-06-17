import sys

N,M= map(int,sys.stdin.readline().split())
l=[]
for i in range(N):
    l.append(list(map(int,sys.stdin.readline().split())))
ans=0
for i in range(N):
    for j in range(M - 3):
        ans = max(sum(l[i][j:j + 4]), ans)
for i in range(N-3):
    for j in range(M):
        ans = max(l[i][j]+l[i+1][j]+l[i+2][j]+l[i+3][j], ans)
for i in range(N-1):
    for j in range(M-1):
        ans=max(l[i][j]+l[i][j+1]+l[i+1][j]+l[i+1][j+1],ans)
for i in range(N-2):
    for j in range(M-1):
        ans=max(l[i][j]+l[i+1][j]+l[i+2][j]+l[i+2][j+1],ans)
        ans=max(l[i][j+1]+l[i+1][j+1]+l[i+2][j+1]+l[i+2][j],ans)
        ans=max(l[i][j]+l[i][j+1]+l[i+1][j]+l[i+2][j],ans)
        ans=max(l[i][j]+l[i][j+1]+l[i+1][j+1]+l[i+2][j+1],ans)
for i in range(N-1):
    for j in range(M-2):
        ans=max(l[i][j]+l[i][j+1]+l[i][j+2]+l[i+1][j],ans)
        ans=max(l[i+1][j]+l[i+1][j+1]+l[i+1][j+2]+l[i][j+2],ans)
        ans=max(l[i+1][j]+l[i+1][j+1]+l[i+1][j+2]+l[i][j],ans)
        ans=max(l[i][j]+l[i][j+1]+l[i][j+2]+l[i+1][j+2],ans)
for i in range(N-2):
    for j in range(M-1):
        ans=max(l[i][j]+l[i+1][j]+l[i+1][j+1]+l[i+2][j+1],ans)
        ans=max(l[i][j+1]+l[i+1][j]+l[i+1][j+1]+l[i+2][j],ans)
for i in range(N-1):
    for j in range(M-2):
        ans=max(l[i][j+1]+l[i][j+2]+l[i+1][j]+l[i+1][j+1],ans)
        ans=max(l[i][j]+l[i][j+1]+l[i+1][j+1]+l[i+1][j+2],ans)
for i in range(N-1):
    for j in range(M-2):
        ans=max(l[i][j+1]+sum(l[i+1][j:j+3]),ans)
        ans=max(l[i+1][j+1]+sum(l[i][j:j+3]),ans)
for i in range(N-2):
    for j in range(M-1):
        ans=max(l[i][j]+l[i+1][j]+l[i+2][j]+l[i+1][j+1],ans)
        ans=max(l[i][j+1]+l[i+1][j+1]+l[i+2][j+1]+l[i+1][j],ans)
print(ans)