n=int(input())
e,o=0,0
l=list(map(int,input().split()))
for i in l:
   if i%2==0:
       e+=i
   else:
       o+=i
print(abs(e-o))