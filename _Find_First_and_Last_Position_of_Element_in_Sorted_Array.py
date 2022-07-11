n=int(input())
l=list(map(int,input().split()))
k=int(input())
t=[]
if k not in l:
    print(-1,-1)
else:
    t.append(l.index(k))
    c=0
    for i in range(n):
        if l[i]==k:
            c=i
    t.append(c)
    print(*t)