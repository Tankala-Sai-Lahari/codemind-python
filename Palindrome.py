n=int(input())
if n>=0:
    print(n==int(str(n)[::-1]))
else:
    print(n==-1*int(str(n[1::][::-1])))