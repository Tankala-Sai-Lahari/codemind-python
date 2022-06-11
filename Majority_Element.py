n=int(input())
l=list(map(int,input().split()))
c=0
i=0
for i in l:
    if l.count(i)>c:
        c=l.count(i)
        e=i
print(e)