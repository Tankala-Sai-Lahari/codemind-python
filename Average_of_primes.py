n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        s.append(i)
if 1 in s:
    s.remove(1)
d=sum(s)/len(s)
print("%.2f"%d)
