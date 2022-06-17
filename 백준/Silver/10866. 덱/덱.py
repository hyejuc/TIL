import sys

N=int(sys.stdin.readline())
d=[]
t=[]
for i in range(N):
    a=sys.stdin.readline().strip()
    if 'push' in a:
        if 'front' in a:
            t.append(a[11:])
            t+=d
            d=t
            t = []
        elif 'back' in a:
            d.append(a[10:])
    if 'pop' in a:
        if 'front' in a:
            if d:
                print(d.pop(0))
            else:
                print(-1)
        else:
            if d:
                print(d.pop())
            else:
                print(-1)
    if a=='size':
        print(len(d))
    if a=='empty':
        if d:
            print(0)
        else:
            print(1)
    if a=='front':
        if d:
            print(d[0])
        else:
            print(-1)
    if a=='back':
        if d:
            print(d[-1])
        else:
            print(-1)