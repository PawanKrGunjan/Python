
'''
Find the smallest number such that the sum of its digits is N and it is divisible by 10^N.
'''
# Method :1
class Solution:
	def digitsNum(self, N):
		# Code here
		return int(str(N%9)+str(9)*(N//9)) * (10**N)
os = Solution()
print(os.digitsNum(500))

# Method : 2
def start(N,n):
    if N <10:
        i = N
    else:
        r = N%10
        i = (10**n)*n + (10**n)*r + int(str(9)*n)
    return i

def digitsum(i):
    l = list(str(i))
    c = l.count('9')
    if c==len(l):
        digisum = 9*c
    else:
        digisum = 9*c + int(l[0])
    return digisum

class Solution:
    def digitsNum(self,N):
        n = N//10
        i = start(N,n)
        num = 10**N
        ds = 0
        f = 10**n
        while ds != N:
            ds = digitsum(i)
            i+=f
        return  (i-f)*num
ob = Solution()
print(ob.digitsNum(500))

if os.digitsNum(500) == ob.digitsNum(500):
    print('True')