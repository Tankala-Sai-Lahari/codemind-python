n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
for i in l:
    if i<a or i>b:
        s.append(i)
if len(s)>0:
    print(*s)
else:
    print(-1)