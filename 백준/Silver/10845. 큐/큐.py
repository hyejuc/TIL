import sys

q=[]
N=int(sys.stdin.readline())
for i in range(N):
    x=sys.stdin.readline().strip()
    if 'push' in x:
        q.append(x[5:])
    elif x=='pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)
    elif x=='size':
        print(len(q))
    elif x=='empty':
        if q:
            print(0)
        else:
            print(1)
    elif x=='front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif x=='back':
        if q:
            print(q[-1])
        else:
            print(-1)