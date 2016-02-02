n = 1041
k = 1
b = 0
p = 0
m = 0
while n != 0:
    while k * 2 <= n:
        k = k * 2
        b = b + 1
    if p - b - 1 > m:
        m = p - b - 1
    p = b
    n = n - k
    k = 1
    b = 0
print m
