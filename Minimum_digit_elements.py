n=int(input())
l=list(map(int,input().split()))
s=len(str(min(l)))
c=0
for i in l:
    if len(str(i))==s:
        c+=1
print(c)