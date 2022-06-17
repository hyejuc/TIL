import sys

while True:
    res=[0]*4
    s=list(sys.stdin.readline())
    if not s:
        break
    for i in s:
        if 'a'<=i<='z':
            res[0]+=1
        elif 'A'<=i<='Z':
            res[1]+=1
        elif i.isdigit():
            res[2]+=1
        elif i==' ':
            res[-1]+=1
    print(*res)