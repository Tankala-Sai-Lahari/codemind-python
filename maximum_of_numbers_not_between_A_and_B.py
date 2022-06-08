n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=0
for i in l:
    if i<a or i>b:
        if m<i:
            m=i
if m>=1:
    print(m)
else:
    print(-1)