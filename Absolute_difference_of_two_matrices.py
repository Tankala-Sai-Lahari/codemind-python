n=int(input())
l,t=[],[]
for i in range(n):
    e=list(map(int,input().split()))
    l.append(e)
for i in range(n):
    e=list(map(int,input().split()))
    t.append(e)
s=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(abs(l[i][j]-t[i][j]))
    s.append(a)
for i in s:
    print(*i)