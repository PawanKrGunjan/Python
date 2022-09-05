# Method : 1
class Solution:
    def smallestSumSubarray(self, A, N):
        Sum = [A[0]]
        for i in range(1,N):
            if Sum[i-1]+A[i] < A[i]:
                Sum.append(Sum[i-1]+A[i])
            else:
                Sum.append(A[i])
        return min(Sum) 

A = [3,-4, 2,-3,-1, 7,-5]
A = [2, 6, 8, 1, 4]
A = [-123, -316]
O = Solution()
S = O.smallestSumSubarray(A, len(A))
print(S)

# Method : 2
class Solution:
    def smallestSumSubarray(self, A, N):
        Sum = []
        for i in range(N):
            Sum.append(sum(A[:i+1]))
            Sum.append(sum(A[i:]))
            for j in range(i+1,N):
                Sum.append(sum(A[i:j]))
        return min(Sum)

#A = [3,-4, 2,-3,-1, 7,-5]
O = Solution()
S = O.smallestSumSubarray(A, len(A))
print(S)