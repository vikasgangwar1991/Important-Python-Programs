#fabonacci series
#0 1 1 2 3 5 8 13 21
a=0
b=1
print(a, b,end=" ")
def fabonacci(n):
    global a,b
    if n>2:
        c=a+b
        print(c,end=" ")
        a=b
        b=c
    return fabonacci(n-1)
fabonacci(10)