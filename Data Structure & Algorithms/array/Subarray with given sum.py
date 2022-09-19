# Method :1
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        for i in range(n):
            S = arr[i]
            for j in range(i+1,n+1):
                if S == s:
                    return i+1,j
                if S > s or j == n:
                    break
                S = S + arr[j]
        return -1, 
    

#A = [int(i) for i in input().split()]
A = [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
#A = [142, 112, 54, 69, 148, 45, 63, 158, 38, 60, 124, 142, 130, 179, 117, 36, 191, 43, 89, 107, 41, 143, 65, 49, 47, 6, 91, 130, 171, 151, 7, 102, 194, 149, 30, 24, 85, 155, 157, 41, 167, 177, 132, 109, 145, 40, 27, 124, 138, 139, 119, 83, 130, 142, 34]

n = len(A)
s = 468
o = Solution()
print(o.subArraySum(A,n,s))


# Method :2
class Solution:
    def subArraySum(self,arr, n, s): 
        S = arr[0]
        Start = 0
        i = 1
        while i <=n:
            while S > s and Start < i-1:
                S = S - arr[Start]
                Start +=1
            
            if S == s:
                return Start+1, i
            if i<n:
                S = S + arr[i]
            i+=1
        return -1, 


ob = Solution()
print(ob.subArraySum(A,n,s))
