def prime(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True
n=int(input())
if prime(n) and prime(int(str(n)[::-1])):
    print("circular prime")
elif prime(n):
    print("prime but not a circular prime")
else:
    print("not prime")