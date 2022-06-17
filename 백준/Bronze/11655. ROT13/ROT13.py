import sys

S=list(sys.stdin.readline().rstrip())
res=[]
for i in S:
    if i.isupper():
        if ord(i)+13>90:
            res.append(chr(ord(i) + 13 - 26))
        else:
            res.append(chr(ord(i)+13))
    elif i.islower():
        if ord(i)+13>122:
            res.append(chr(ord(i) + 13 - 26))
        else:
            res.append(chr(ord(i)+13))
    else:
        res.append(i)
print(''.join(res))