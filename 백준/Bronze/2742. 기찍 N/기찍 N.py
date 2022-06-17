import sys

N=int(sys.stdin.readline())
a=1
for i in range(N,0,-1):
    print(a*i)
    i-=1