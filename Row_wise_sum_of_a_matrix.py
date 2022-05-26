n,m=map(int,input().split())
l=[]
s=[]
for i in range(n):
    t=list(map(int,input().split()))
    l.append(t)
for i in range(n):
    c=0
    for j in range(m):
       c+=l[i][j]
    s.append(c)
print(*s)
    