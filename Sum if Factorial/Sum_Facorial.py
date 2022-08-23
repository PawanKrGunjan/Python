import math

def factDigit(N):
    result = []
    for i in reversed(range(9)):
        f = math.factorial(i)
        if N >= f:
            N -= f
            result.append(i+1)
            break
    return result[::-1]

def FactDigit(N):
    n = 0
    f = sum([math.factorial(int(i)) for i in str(n)])
    while N != f:
        n += 1
        f = sum([math.factorial(int(i)) for i in str(n)])
    return n



print(factDigit(40345))  
print(factDigit(362881)) 
print(factDigit(363000))

print(FactDigit(40345))  
print(FactDigit(362881)) 
print(FactDigit(363000))