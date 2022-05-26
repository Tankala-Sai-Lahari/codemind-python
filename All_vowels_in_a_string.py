s=input()
l=[]
for i in s:
    if i in "AEIOUaeiou" and i not in l:
        l.append(i)
for i in "aeiou":
    if i not in l:
        print("False")
        break
else:
    print("True")