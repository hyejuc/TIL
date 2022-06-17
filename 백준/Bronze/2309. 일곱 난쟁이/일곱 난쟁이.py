h=[]
for i in range(9):
    h.append(int(input()))
for i in range(9):
    if len(h)==7:
        break
    else:
        for j in range(i + 1, 9):
            if h[i] + h[j] == sum(h) - 100:
                h.pop(j)
                h.pop(i)
                break
for i in sorted(h):
    print(i)