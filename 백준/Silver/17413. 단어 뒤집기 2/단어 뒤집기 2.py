import sys

S=list(sys.stdin.readline().strip())
res=[]
word=[]
while S:
    if S[0] == '<':
        res.append(S.pop(0))
        while S[0] != '>':
            res.append(S.pop(0))
        res.append(S.pop(0))
    else:
        while S[0]!='<':
            word.append(S.pop(0))
            if len(S)==0:
                break
            elif S[0]==' ':
                break
        while word:
            res.append(word.pop())
        if len(S)==0:
            break
        elif S[0]==' ':
            res.append(S.pop(0))
for i in res:
    print(i,end='')