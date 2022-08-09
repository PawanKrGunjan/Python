from ast import While


class Solution:	
    #Function to reverse every sub-array group of size k.
    '''
	def reverseInGroups(self, arr, N, K):
        # code here
        i = 0
        while (i<N):
            left = i
            right = min(i + K - 1, N - 1)

            # Reverse the sub-array [left, right]
            while (left < right):
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            i+= K
    '''
    def reverseInGroups(arr, N, K):
        r = [arr[i] for i in range(K)]
        r.reverse()
        for i in range(N-K+1):
            r.append(arr[-i])
        return r


import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()