def d(n):
    a=[n]
    for i in range(len(str(n))):
        a.append(int(str(n)[i]))
        i+=1
    return sum(a)
A=set()
for j in range(1,10001):
    A.add(d(j))
    j+=1
for k in range(1,10001):
    if k in A:
        pass
    else:
        print(k)
    k+=1