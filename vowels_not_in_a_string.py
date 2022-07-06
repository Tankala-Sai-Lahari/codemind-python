s=input()
v=""
for i in "aeiou":
    if i not in s:
        v+=i
if len(v)>0:
    for i in v:
        print(i,end=" ")
else:
    print(0)