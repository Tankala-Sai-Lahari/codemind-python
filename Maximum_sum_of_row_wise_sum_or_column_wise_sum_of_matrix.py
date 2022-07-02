n,m=map(int,input().split())
l,r=[],[]
for i in range(n):
    t=list(map(int,input().split()))
    l.append(t)
    r.append(sum(t))
c=[]
for i in range(m):
    p=[]
    for j in range(n):
        p.append(l[j][i])
    c.append(sum(p))
print(max(c+r))