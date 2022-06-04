def prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    else:
        return True
num=int(input())
s=0
for j in range(0,num):
    if prime(num-j):
        s=num-j
        break
    elif prime(num+j):
        s=num+j
        break
print(abs(num-s))