n,m=map(int,input().split())
l=[]
s=[]
for i in range(n):
    t=list(map(int,input().split()))
    l.append(t)
for i in range(m):
    c=0
    for j in range(n):
       c+=l[j][i]
    s.append(c)
print(max(s))
    