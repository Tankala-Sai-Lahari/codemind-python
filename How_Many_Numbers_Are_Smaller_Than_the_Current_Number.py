n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(n):
    c=0
    for j in range(n):
        if j!=i:
            if l[i]>l[j]:
                c+=1
    r.append(c)
print(*r)