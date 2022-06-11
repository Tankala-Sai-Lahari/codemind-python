n=int(input())
l=list(map(int,input().split()))
for j in range(n):
    for i in range(n-1):
        if l[i]==0:
            l[i],l[i+1]=l[i+1],l[i]
print(*l)