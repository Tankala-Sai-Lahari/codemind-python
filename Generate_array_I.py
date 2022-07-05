n=int(input())
l=list(map(int,input().split()))
t=[]
for i in range(0,n,2):
    for j in  range(l[i+1]):
        t.append(l[i])
print(*t)