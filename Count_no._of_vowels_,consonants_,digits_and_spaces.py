s=input()
c,v,d,w=0,0,0,0
for i in s:
    if  i in "qwrtypsdfghjklxcvbnmQWRTYPSDFGHJKLZXCVBNM":
        c+=1
    elif  i in "aeiouAEIOU":
        v+=1
    elif i.isdigit():
        d+=1
    elif i==" ":
        w+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",w)
