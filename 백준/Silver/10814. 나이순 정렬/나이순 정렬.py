import sys

N=int(sys.stdin.readline())
a=[]
for i in range(N):
    x,y=sys.stdin.readline().split()
    a.append([int(x),str(y).strip()])
a.sort(key=lambda x:(x[0]))
for i in range(len(a)):
    print(a[i][0],a[i][1])