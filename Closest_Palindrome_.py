def ispallendrome(num):
    if num>0:
        return num==int(str(num)[::-1])
    elif n<0:
        return num==-1*int(str(num)[1::-1])
    else:
        return True
n=int(input())
r=0
for i in range(1,n):
    if ispallendrome(n-i):
        print(n-i,end=" ")
        r+=1
    if ispallendrome(n+i):
        print(n+i,end=" ")
    if r==1:
        break
