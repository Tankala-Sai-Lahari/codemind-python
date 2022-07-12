n=int(input())
l=[]
s1,s2=0,0
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if i==j :
            s1+=l[i][j]
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            s2+=l[i][j]

print("Principal Diagonal:",s1,sep="")
print("Secondary Diagonal:",s2,sep="")