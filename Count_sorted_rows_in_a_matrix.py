n,m=map(int,input().split())
c=0
for i in range(n):
    t=list(map(int,input().split()))
    if t==sorted(t) or t==sorted(t)[::-1]:
        c+=1
print(c)