from typing import List
from collections import deque
class Solution:
    def isStackPermutation(self, N : int, A : List[int], B : List[int]) -> int:
        # code here
        stack = deque()
        for i in range(N):
            stack.append(A[i])

        b = deque()
        for i in range(N):
            b.append(B[i])

        # Stack to be used for permutations
        t = []
        while stack.em:
            pass

# Given two arrays, check if one array is
# stack permutation of other.
from queue import Queue

# function to check if Input queue
# is permutable to output queue
def checkStackPermutation(ip, op, n):
	
	# Input queue
	Input = Queue()
	for i in range(n):
		Input.put(ip[i])

	# output queue
	output = Queue()
	for i in range(n):
		output.put(op[i])

	# stack to be used for permutation
	tempStack = []
	while (not Input.empty()):
		ele = Input.queue[0]
		Input.get()
		if (ele == output.queue[0]):
			output.get()
			while (len(tempStack) != 0):
				if (tempStack[-1] == output.queue[0]):
					tempStack.pop()
					output.get()
				else:
					break
		else:
			tempStack.append(ele)

	# If after processing, both Input
	# queue and stack are empty then
	# the Input queue is permutable
	# otherwise not.
	return (Input.empty() and
		len(tempStack) == 0)

# Driver Code
if __name__ == '__main__':

	# Input Queue
	Input = [1, 2, 3]

	# Output Queue
	output = [2, 1, 3]

	n = 3

	if (checkStackPermutation(Input,
							output, n)):
		print("Yes")
	else:
		print("Not Possible")

# This code is contributed by PranchalK
