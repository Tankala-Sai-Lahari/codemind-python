def fib(num):
    l=[0,1]
    while l[-1]<=num:
        l.append(l[-1]+l[-2])
    return l[-2]==num
num=int(input())
print(fib(num))
