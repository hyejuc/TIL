import sys

a=[]
N=int(sys.stdin.readline())
for i in range(N):
    a.append(list(map(int,sys.stdin.readline().split())))
a.sort(key=lambda x:(x[0],x[1]))
for i in range(len(a)):
    print(a[i][0],a[i][1])