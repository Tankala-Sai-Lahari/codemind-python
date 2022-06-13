n,m=map(int,input().split())
l1=[n*i for i in range(1,n*n) ]
l2=[m*i for i in range(1,m*m)]
for i in l1:
    if i in l2:
        print(i)
        break
