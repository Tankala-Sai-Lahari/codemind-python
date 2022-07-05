n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    l1.append(len(str(i)))
m=max(l1)
for i in l:
    if m==len(str(i)):
        print(i,end=" ")