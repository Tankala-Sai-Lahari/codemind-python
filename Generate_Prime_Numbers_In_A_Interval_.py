def prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    else:
        return True
m=int(input())
n=int(input())
for i in range(m,n+1):
    if prime(i):
        print(i)
