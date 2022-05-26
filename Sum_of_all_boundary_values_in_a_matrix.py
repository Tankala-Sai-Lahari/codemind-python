n,m=map(int,input().split())
s=[]
for i in range(n):
    k=list(map(int,input().split()))
    s.append(k)
sum1=0
for i in range(n):
    for j in range(m):
        if i==0 or j==0 or j==m-1 or i==n-1:
            sum1+=s[i][j]
print(sum1)