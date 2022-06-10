n=int(input())
if n**2==int(str(int(str(n)[::-1])**2)[::-1]):
    print(True)
else:
    print(False)