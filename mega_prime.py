def prime(num):
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        else:
            return True
    else:
        return False
num=int(input())
if prime(num): 
    while num>0:
        if not(prime(num%10)):
            print("Not Mega Prime")
            break
        num//=10
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")
    