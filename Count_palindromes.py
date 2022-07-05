n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if i==int(str(i)[::-1]):
        c+=1
print(c)