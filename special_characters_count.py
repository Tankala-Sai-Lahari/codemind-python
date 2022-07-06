s=input()
c=0
for i in s:
    if i not in "Q WERTYUIOPASDFGHJKLZXCVBNMqwertyuiopsdfghjklzxcvbnma1234567890":
        c+=1
print(c)