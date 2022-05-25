a,b=map(int,input().split())
l=list(map(int,input().split()))
f=list(map(int,input().split()))
c=[]
for i in l:
    if i in f and i not in c:
        c.append(i)
for i in f:
    if i in l and i not in c:
        c.append(i)       
print(*c)