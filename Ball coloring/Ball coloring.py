#User function Template for python3
from itertools import permutations, combinations
class Solution:
    def noOfWays (self, n):
        # code here 
        l = []
        for i in range(n):
            l.append('r')
            l.append('b')
        if n == 1:
            L = list(permutations(l,n))
        else:
            L = list(combinations(l,n))
        L = sorted(L)
        i = 0
        for i in range(len(L)):
            
        print(L)
        return len(L)

if __name__ == '__main__': 

    n = 4 #int(input())
        
    ob = Solution()
    print(ob.noOfWays(n))
