import sys

S=sys.stdin.readline().strip()
res=[]
for i in range(len(S)):
    res.append(S[i:])
for i in sorted(res):
    print(i)