import sys

N=int(sys.stdin.readline())
a=[]
for i in range(N):
    X=sys.stdin.readline().strip()
    if 'push' in X:
        a.append(int(str(X[5:])))
    elif 'pop' == X:
        if len(a)==0:
            print(-1)
        else:
            print(a[-1])
            a.pop()
    elif 'size' ==X:
        print(len(a))
    elif 'empty'==X:
        if len(a)==0:
            print(1)
        else:
            print(0)
    elif 'top'==X:
        if len(a)==0:
            print(-1)
        else:
            print(a[-1])