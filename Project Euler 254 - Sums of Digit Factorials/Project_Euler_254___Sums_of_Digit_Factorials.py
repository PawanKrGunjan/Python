print("Project Euler #254: Sums of Digit Factorials : https://www.hackerrank.com/contests/projecteuler/challenges/euler254/problem?isFullScreen=false")
def gn(N):
    n = 1
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    fn = sum([factorials[int(i)] for i in str(n)])
    sn = sum([int(i) for i in str(fn)])
    while sn != N:
        n += 1
        sn = sum([int(i) for i in str(sum([factorials[int(i)] for i in str(n)]))])
    return n

def sgn(n):
    sgn = 0
    for i in range(1,n+1):
        sgn +=sum([int(i) for i in str(gn(i))])
    return sgn
       
print("Enter the number of test:")
t = int(input())
for i in range(t):
    n = int(input())
    print(sgn(n))