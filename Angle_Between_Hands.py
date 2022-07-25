h,m=map(int,input().split(":"))
if h==12:
    h=0
if m==60:
    m=0
    h+=1
    if h==12:
        h-=12
ah=0.5*(h*60+m)
am=6*m
angle=abs(ah-am)
print(min(360-angle,angle))