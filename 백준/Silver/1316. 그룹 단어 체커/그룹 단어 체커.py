import sys
N=int(sys.stdin.readline())
c=0
for i in range(N):
    X=sys.stdin.readline().strip()
    x=list()
    for l in list(X):
        if l not in x:
            x.append(l)
    for j in x:
        if j == X[0]:
            if X.count(j) == 1:
                X=X[1:]
            else:
                X=X[X.count(j):]
    if X=='':
        c+=1
print(c)