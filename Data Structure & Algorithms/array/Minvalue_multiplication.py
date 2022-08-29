def minValue(a, b, n):
        # Your code goes here
        A = sorted(a)
        B = sorted(b)
        m = 0
        for i in range(n):
            m += A[i] * B[n-1-i]
        return m

a = [3,1,1]
b = [6,5,4]
n = 3
print(minValue(a,b,n))