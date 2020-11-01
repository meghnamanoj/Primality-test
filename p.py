''' Miller-Rabin primality test''' 
n = int(input('Enter a no greater than 2 : '))
x = n-1
y = x
k = 0
while x%2 == 0:
    x = x//2
    k = k+1
m = y/(2**k)
a =2
i = 0
s = a**((2**i)*m)
b = s%n
if b == 1 or b == -1:
    print(str(n)+' is probably prime')
else :
    while i in range(0,k):
        i = i+1
        s = a**((2**i)*m)
        b = s%n
        if b == n-1:
            break
    if b == n-1 or b == 1:
        print(str(n)+' is probably prime')
    else: 
        print(str(n)+' is composite')
