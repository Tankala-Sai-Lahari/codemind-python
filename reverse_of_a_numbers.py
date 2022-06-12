n=int(input())
if n>0:
    print(int(str(n)[::-1]))
elif n<0:
    print(-1*int(str(n)[1::-1]))
else:
    print(0)
