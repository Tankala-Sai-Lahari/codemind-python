def prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    else:
        return True
m=int(input())
if prime(m) and prime(int(str(m)[::-1])):
    print("circular prime")
elif prime(m) and not(prime(int(str(m)[::-1]))):
    print("prime but not a circular prime")
else:
    print("not prime")