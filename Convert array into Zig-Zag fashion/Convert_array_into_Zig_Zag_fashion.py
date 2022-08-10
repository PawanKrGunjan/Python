'''
Given an array Arr (distinct elements) of size N. 
Rearrange the elements of array in zig-zag fashion. 
The converted array should be in form a < b > c < d > e < f. 
The relative order of elements is same in the output 
i.e you have to iterate on the original array only.
'''
print("Convert array into Zig-Zag fashion")

class Solution:
	def zigZag(self,arr, n):
		# code here
		for i in range(n-1):
			a = arr[i]
			b = arr[i+1]
			if i%2 == 0:
				if a>b:
					arr[i]=b
					arr[i+1]=a
			else:
				if a<b:
					arr[i]=b
					arr[i+1]=a
		return arr

if __name__ == '__main__':
	print('Size of distinct element (n=7)')
	n = int(input())
	print("Enter the distinct element (4 3 7 8 6 2 1)")
	arr = list(map(int, input().strip().split()))
	ob = Solution()
	ob.zigZag(arr, n)
	for x in arr:
		print(x, end=" ")

