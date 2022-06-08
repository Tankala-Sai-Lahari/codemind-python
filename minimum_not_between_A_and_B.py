n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=max(l)
for i in l:
    if i<a or i>b:
        if i<m:
            m=i
if m==max(l):
    print(-1)
else:
    print(m)