n=input()
t=""
for i in n:
    if i not in t:
        t+=i
if t==n:
    print("Unique Number")
else:
    print("Not Unique Number")