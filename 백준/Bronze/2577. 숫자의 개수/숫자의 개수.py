import sys

A=int(sys.stdin.readline())
B=int(sys.stdin.readline())
C=int(sys.stdin.readline())
X=str(A*B*C)
a=list()
for i in range(0,len(X)):
    a.append(int(X[i]))
    i+=1
for j in range(0,10):
    print(a.count(j))
    j+=1
