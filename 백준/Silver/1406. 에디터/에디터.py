import sys

x=list(sys.stdin.readline().strip())
x2=[]
M=int(sys.stdin.readline())
for i in range(M):
    a=sys.stdin.readline().strip()
    if a=='L':# a b a /e d
        if x:
            x2.append(x.pop())
    elif a=='D':
        if x2:
            x.append(x2.pop())
    elif a=='B':
        if x:
            x.pop()
    elif 'P' in a:
        x.append(a[-1])
x.extend(reversed(x2))
print(''.join(x))
