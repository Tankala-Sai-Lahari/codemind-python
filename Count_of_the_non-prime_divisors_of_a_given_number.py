def prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    else:
        return True
m=int(input())
c=0
for i in range(1,m+1):
    if m%i==0 and not(prime(i)):
        c+=1
print(c)