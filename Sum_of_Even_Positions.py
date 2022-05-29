n=int(input())
s=0
l=list(map(int,input().split()))
for i in range(0,n,2):
    s+=l[i]
print(s)