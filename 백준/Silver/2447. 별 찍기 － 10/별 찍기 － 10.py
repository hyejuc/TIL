def star(N):
    s=list()
    for i in range(len(S)*3):
        if i//len(S)==1:
            s.append(S[i%len(S)]+' '*len(S)+S[i%len(S)])
        else:
            s.append(S[i%len(S)]*3)
    return s

S=['***','* *','***']
N=int(input())
cnt=0
while N!=3:
    N=int(N/3)
    cnt+=1
for i in range(cnt):
    S=star(S)
for i in S:
    print(i)