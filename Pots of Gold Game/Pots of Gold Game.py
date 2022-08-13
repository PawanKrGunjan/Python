'''
Two players X and Y are playing a game in which there are pots of gold arranged in a line, 
each containing some gold coins. 
They get alternating turns in which the player can pick a pot from one of the ends of the line. 
The winner is the player who has a higher number of coins at the end. 
The objective is to maximize the number of coins collected by X, assuming Y also plays optimally.

Return the maximum coins X could get while playing the game. Initially, X starts the game.
'''
print('Pots of Gold Game')
print(''' Input Example:
        (t=4

        n=9
        arr{}=15 11 5 14 13 12 20 10 20
        Output= 67

        n=4
        arr{}=8 15 3 7
        output = 22

        n=7
        arr{}=3 16 14 7 5 8 16
        output = 38

        n=4
        arr{}=2 2 2 2
        output = 4
        ''')
        
class Solution:
    def maxCoins(self, arr, n):
        # Code here
        t = [[ 0 for i in range(n)] for j in range(n)]
        print(t)
        for g in range(n):
            i=0
            j=g
            while(j<n):
                if(i+2 <= j):
                    x = t[i+2][j]
                else:
                    x = 0
                if(i+1 <= j-1):
                    y = t[i+1][j-1]
                else:
                    y = 0
                if(i <= j-2):
                    z = t[i][j-2]
                else:
                    z = 0
                t[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
                i+=1
                j+=1
            print(t)
        return t[0][n-1]
 

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxCoins(arr, n))