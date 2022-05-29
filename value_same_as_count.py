n=int(input())
l=list(map(int,input().split()))
t=[]
c=[]
for i in l:
    if i not in t:
        t.append(i)
        if l.count(i)==i:
            c.append(l.count(i))
f=0
if len(c)>0:
    for i in t:
        if i==l.count(i):
            f+=1
print(f)
