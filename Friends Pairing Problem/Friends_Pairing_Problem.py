print('''
Given N friends, each one can remain single or can be paired up with some other friend. 
Each friend can be paired only once. 
Find out the total number of ways in which friends can remain single or can be paired up.
Note: Since answer can be very large, return your answer mod 10^9+7.
''')

class Solution:
    def countFriendsPairings(self, n):
        #l = [0  for i in range(n+1)]
        a, b, c = 1, 2, 0
        
        if n<=2 :
            return n
        for i in range(3, n+1):
            c =  b + (i-1)* a
            a = b
            b = c
        return c % 1000000007

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    n = int(input())
    ob = Solution()
    print(ob.countFriendsPairings(n))
