def gcd(a, b):
    for i in range(min(a,b)+1,-1,-1):
        if a%i == 0 and b%i == 0:
            return i

print(gcd(576,786))
print(gcd(76,84))
print(gcd(57,786))
print(gcd(56,76))