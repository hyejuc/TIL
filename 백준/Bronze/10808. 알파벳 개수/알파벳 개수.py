import sys

S=list(sys.stdin.readline().strip())
res=[]
for i in range(26):
    if chr(97+i) in S:
        res.append(S.count(chr(97+i)))
    else:
        res.append(0)
print(*res)