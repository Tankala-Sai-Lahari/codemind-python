n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    c=1
    for j in range(n):
        if i!=l[j]:
            c*=l[j]
    l1.append(c)
print(*l1)