n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(0,n,2):
    for j in range(l[i+1]):
        s.append(l[i])
print(*s)