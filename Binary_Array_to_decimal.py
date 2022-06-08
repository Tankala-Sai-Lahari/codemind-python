n=int(input())
l=list(map(int,input().split()))
s=0
n-=1
for i in l:
    if i==1:
        s+=2**n
    n-=1
print(s)