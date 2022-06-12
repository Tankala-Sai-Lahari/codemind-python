def num(n):
    l=list(str(n))
    c=0
    for i in l:
        i=int(i)
        if i!=0 and n%i==0:
            c+=1
    if c==len(l):
        return True
    else:
        return False
n=int(input())
m=int(input())
for i in range(n,m+1):
    if num(i):
        print(i,end=" ")
