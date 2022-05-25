n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if str(i)[::-1]==str(i):
        c+=1
print(c)