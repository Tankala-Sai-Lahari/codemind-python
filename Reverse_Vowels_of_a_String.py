s=input()
l=[]
for i in s:
    if i in "aeiouAEIOU":
        l.append(i)
l=l[::-1]
e=""
j=0
for i in s:
    if i in "aeiouAEIOU":
        e+=l[j]
        j+=1
    else:
        e+=i
print(e)