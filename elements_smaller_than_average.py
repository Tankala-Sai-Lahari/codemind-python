n=int(input())
l=list(map(int,input().split()))
a=sum(l)//n
c=0
for i in l:
    if i<=a:
        c+=1
print(c)