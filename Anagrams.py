l1=list(input().lower())
t1=list(input().lower())

for i in l1+t1:
    if i not in t1 or i not in l1:
        print(False)
        break
else:
    print(True)
