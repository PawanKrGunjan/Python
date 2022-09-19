

# Method : 1
class Solution:
    def pattern(self, n):
        N = n*(n+1)
        l = [i for i in range(1,N+1)]
        result = []
        for i in range(n):
            S ='--'*i
            for j in range(n-i):
                S +=str(l[0])
                l.remove(l[0])
                S +='*'
            for k in range(n-i):
                S +=str(l[-n+k+i])
                l.remove(l[-n+k+i])
                if n-i-k > 1:
                    S += '*'
            result.append(S)
        return result

n = 10
ob = Solution()
r = ob.pattern(n)
for i in range(n):
    print(r[i])

print()
# Method :2
class Solution:
    def pattern(self, n):
        N = n*(n+1)
        l = [i for i in range(1,N+1)]
        for i in range(n):
            print('  '*i,end='')
            for j in range(n-i):
                print(l[0],end='')
                l.remove(l[0])
                print('*',end='')
            for k in range(n-i):
                print(l[-n+k+i],end='')
                l.remove(l[-n+k+i])
                if n-i-k > 1:
                    print('*', end = '')
                else:
                    print()

os = Solution()
os.pattern(10)
