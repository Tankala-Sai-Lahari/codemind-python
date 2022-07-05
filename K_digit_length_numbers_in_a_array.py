n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if i>=0 and len(str(i))==m:
        c+=1
    elif i<0 and len(str(i))==m+1:
        c+=1
print(c)