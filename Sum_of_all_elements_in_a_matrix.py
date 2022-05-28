n,m=map(int,input().split())
l=[]
for i in range(n):
    l.extend(list(map(int,input().split())))
print(sum(l))