import sys

N=int(sys.stdin.readline())
x=0
for i in range(1,N+1):
    if i+sum(list(map(int,str(i))))==N:
        x+=i
        break
print(x)