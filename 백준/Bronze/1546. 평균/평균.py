import sys

N=int(sys.stdin.readline())
S=list(map(int,sys.stdin.readline().split()))
M=max(S)
X=list()
for i in range(0,N):
    x=(S[i]/M)*100
    X.append(x)
    i+=1
print(sum(X)/len(X))