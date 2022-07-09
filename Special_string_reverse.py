s=input()
l=[]
j=0
for i in s:
    if i.isalpha():
        l.append(i)
l=l[::-1]
e=''
for i in s:
    if i.isalpha():
        e+=l[j]
        j+=1
    else:
        e+=i
print(e)