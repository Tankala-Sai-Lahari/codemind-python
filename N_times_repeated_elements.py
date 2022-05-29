n=int(input())
l=list(map(int,input().split()))
k=int(input())
t=[]
for i in l:
    if i not in t and l.count(i)==k:
        t.append(i)
if len(t)>0:
    print(*t)
else:
    print(-1)
        