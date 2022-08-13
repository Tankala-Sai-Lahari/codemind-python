dic={0:"000",1:"001",2:"010",3:"011",4:"100",5:"101",6:"110",7:"111"}
n=int(input())
l=[]
while n>0:
    l.append(dic[n%10])
    n//=10
l=l[::-1]
print(int("".join(l)))