def prime(num):
    if num<=1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        else:
            return True
n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in l:
    if i<=k and prime(i) :
        c+=1
print(c)