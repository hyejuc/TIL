import sys

x=[]
N=int(sys.stdin.readline())
for i in range(N):
    x.append(str(sys.stdin.readline().strip()))
X=list(set(x))
X.sort(key=lambda x:(len(x),x))
for i in X:
    print(i)