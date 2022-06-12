n=int(input())
if n<0:
    t=str(n)[1::]
    print(-1*(int(t[::-1])))
else:
    print(int(str(n)[::-1]))