n,m=map(int,input().split())
l=[]
e,o=0,0
for i in range(n):
    t=list(map(int,input().split()))
    if i%2==0:
        e+=sum(t)
    else:
        o+=sum(t)
print(e,o)
   
    