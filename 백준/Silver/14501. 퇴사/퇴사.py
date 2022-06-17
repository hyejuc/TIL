import sys

N=int(sys.stdin.readline())
l=[]
for i in range(N):
    l.append(list(map(int,sys.stdin.readline().split())))
max_pay=[0]*(N+1)

for i in range(N-1,-1,-1):
    if l[i][0]<=N-i:
        max_pay[i]=max(l[i][1]+max_pay[i+l[i][0]],max_pay[i+1])
    else:
        max_pay[i]=max_pay[i+1]
print(max_pay[0])