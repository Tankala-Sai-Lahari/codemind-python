n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for i in l1+l2:
    if i in l1 and i in l2 and i not in l3:
        l3.append(i)
print(len(l3))