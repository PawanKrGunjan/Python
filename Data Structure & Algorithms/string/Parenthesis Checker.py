
#User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        open = []
        close = []
        parenthesis = ['(',"{","["]
        for i in range(len(x)):
            if x[i] in parenthesis:
                open.append(x[i])
            
            if x[i]==']'and open[-1]=='[':
                open.remove(']')
            elif x[i]=='}'and open[-1]=='{':
                open.remove('{')
            elif x[i]==')'and open[-1]==')':
                open.remove('(')
            
            if open:
                return False

        pass




import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = 1
    for cases in range(test_cases) :
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends