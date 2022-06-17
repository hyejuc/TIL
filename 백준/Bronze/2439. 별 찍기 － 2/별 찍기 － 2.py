import sys

N=int(sys.stdin.readline())
for i in range(1,N+1):
    a="*"*i
    print(a.rjust(N))
    i+=1