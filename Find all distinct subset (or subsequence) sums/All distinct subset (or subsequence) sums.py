print("Wrong")
class Solution:
	def DistinctSum(self, nums):
		# Code here
		nums.sort()
		l = len(nums)
		n = l
		S = set()
		#while n > 1:
		for i in range(l):
			S.add(0)
			S.add(nums[i])
			for j in range(i,l):
				for k in range(i):
					Sum = nums[i] + sum(nums[k:i])

		#n -= 1
		#print(S)
		return S

ob = Solution()
nums = [2, 6, 3, 1, 8, 10, 9, 1, 7]
#nums = [1, 2, 4, 10, 3, 10, 10, 8, 7]
#nums = [3, 6, 10]
#nums = [1,2]
#nums = [1,2,3,4]
print(sorted(nums))
print(ob.DistinctSum(nums))
print('*****')
print(sum(nums))
#print(nums[8])
#print(sum(nums[0:0]) + nums[0])
#print(sum(nums[0:0]))
