import statistics as st
A,B,C=map(int,input().split())
a=[A, B, C]
if A==B or B==C or A==C:
    if A==B==C:
        print(10000+A*1000)
    else:
        print(1000+st.mode(a)*100)
else:
    print(max(a)*100)