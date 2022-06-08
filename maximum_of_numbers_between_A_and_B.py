n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=min(l)
for i in l:
    if i>=a and i<=b:
        if i>m:
            m=i
if m==min(l):
    print(-1)
else:
    print(m)
        