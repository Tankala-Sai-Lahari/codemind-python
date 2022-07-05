n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
t=[]
for i in l1+l2:
    if i in l1 and i in l2:
        l3.append(i)
    if i not in t:
        t.append(i)
for i in t:
    if i not in l3:
        print(i,end=" ")
        