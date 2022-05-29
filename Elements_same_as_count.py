n=int(input())
l=list(map(int,input().split()))
t=[]
c=[]
for i in l:
    if i not in t:
        t.append(i)
        if l.count(i)==i:
            c.append(l.count(i))
if len(c)>0:
    for i in t:
        if i==l.count(i):
            print(i,end=" ")
else:
    print(-1)
