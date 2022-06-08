s=input().split()
t=min(s[-1])
if t.lower() in s[-1]:
    print(t.lower())
else:
    print(t)