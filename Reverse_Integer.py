n=int(input())
if n>0:
    print(int(str(n)[::-1]))
else:
    print(-1*(int(str(-1*n)[::-1])))
