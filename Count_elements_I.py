a,b=map(int,input().split())
l=list(map(int,input().split()))
f=list(map(int,input().split()))
z=list(set(l+f))
c=0
for i in z:
    if i in l and i in f:
        c+=1
print(c)