def prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    else:
        return True
t=int(input())
for i in range(t):
    num=int(input())
    for j in range(0,num):
        if prime(num-j):
            print(num-j)
            break
        elif prime(num+j):
            print(num+j)
            break

        
            