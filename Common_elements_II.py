a,b=map(int,input().split())
l=list(map(int,input().split()))
f=list(map(int,input().split()))
c=[]
for i in l:
    if i not in f:
        c.append(i)
for i in f:
    if i not in l:
        c.append(i)       
print(*c)