import sys

N=int(sys.stdin.readline())
a=list()
for i in range(N):
    x=int(sys.stdin.readline())
    a.append(x)
s=list(set(a))
s.sort()
print(*s,sep='\n')