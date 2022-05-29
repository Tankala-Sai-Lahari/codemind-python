n=int(input())
l=list(map(int,input().split()))
t=[]
for i in l:
    if i not in t and l.count(i)==i:
        t.append(i)
if len(t)>0:
    print("%.2f"%(sum(t)/len(t)),end=" ")
    
else:
    print(-1)
        