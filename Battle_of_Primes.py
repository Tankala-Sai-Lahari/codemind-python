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
for i in range(1,m*n):
    if prime(m+n+i):
        print(i)
        break
