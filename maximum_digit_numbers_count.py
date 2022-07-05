n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(len(str(i)))
length=max(l1)
for i in l:
    if len(str(i))==length:
        print(i,end=" ")