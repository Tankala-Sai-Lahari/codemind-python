s=input()
l=[]
for i in s:
    if i in "AEIOUaeiou":
        l.append(i)
print(len(l))