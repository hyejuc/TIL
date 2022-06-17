import sys

N=int(sys.stdin.readline())
c=[]
for i in range(N):
    c.append(list(sys.stdin.readline().strip()))

def number(c,N):
    count = 1
    for i in range(N):
        temp = 1
        for j in range(1, N):
            if c[i][j] == c[i][j - 1]:
                temp += 1
                count = max(temp, count)
            else:
                temp = 1
        temp = 1
        for j in range(1, N):
            if c[j][i] == c[j - 1][i]:
                temp += 1
                count = max(temp, count)
            else:
                temp = 1
    return count
count=0
for i in range(N):
    for j in range(1,N):
        if c[i][j]!=c[i][j-1]:
            c[i][j], c[i][j - 1] = c[i][j - 1], c[i][j]
            count=max(number(c,N),count)
            c[i][j], c[i][j - 1] = c[i][j - 1], c[i][j]
        if c[j][i]!=c[j - 1][i]:
            c[j][i],c[j-1][i]=c[j-1][i],c[j][i]
            count=max(number(c,N),count)
            c[j][i], c[j - 1][i] = c[j - 1][i], c[j][i]
print(count)