from math import sqrt
class Solution:
    def nineDivisors(self, N):
        # code here 
        nineDivisors = []
        for i in range(1, N+1):
            Divisors = []
            for j in range(1,int(sqrt(i))+1):
                if i%j == 0:
                    Divisors.append(j)
                    Divisors.append(i/j)
            if len(set(Divisors)) == 9:
                nineDivisors.append(i)
        return len(nineDivisors)


if __name__ == '__main__': 
    print("Enter the number of times of test ")
    print("Enter the number upto which we want to find the divisors")
    t = int(input())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.nineDivisors(N))
