import sys

A,B=map(int,sys.stdin.readline().split())
m=int(sys.stdin.readline())
x=list(map(int,sys.stdin.readline().split()))
x.reverse()
a=0
for i in range(m):
    a+=x[i]*(A**i)
res=[]
while a:
    res.append(a%B)
    a//=B
print(*reversed(res))