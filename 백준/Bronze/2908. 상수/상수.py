import sys
A,B=sys.stdin.readline().split()
a=A[::-1]
b=B[::-1]
if a>b:
    print(a)
else:
    print(b)