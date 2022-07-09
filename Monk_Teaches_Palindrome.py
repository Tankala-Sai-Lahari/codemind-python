n=int(input())
for z in range(n):
    s=input()
    if s==s[::-1]:
        print("YES",end=" ")
        if len(s)%2==0:
            print("EVEN")
        else:
            print("ODD")
    else:
        print("NO")