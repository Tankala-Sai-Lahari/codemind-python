n=int(input())
e,o=0,0
while n>0:
    i=n%10
    if i%2==0:
        e+=1
    else:
        o+=1
    n//=10
if e>0 and o>0:
    print("Mixed")
elif e>0 and o==0:
    print("Even")
else:
    print("Odd")